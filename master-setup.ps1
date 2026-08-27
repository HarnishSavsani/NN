#Requires -Version 5.1
# Start-Process powershell -Verb RunAs -ArgumentList "-ExecutionPolicy Bypass -File .\master-setup.ps1"
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# ╔══════════════════════════════════════════════════════════════════╗
# ║  MASTER SETUP SCRIPT — Menu-Driven                             ║
# ║  Combines: Tool Setup + LiteLLM/Langfuse Podman Setup          ║
# ╚══════════════════════════════════════════════════════════════════╝

$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Path
$BASE_URL    = "https://genailab.tcs.in"
$MAX_RETRIES = 3
$ErrorCount  = 0
$SettingsFile = "$env:USERPROFILE\.claude\settings.json"
$ServicesDir  = "$env:USERPROFILE\Documents\hackathon-services"

# ===================================================================
# Shared Helpers
# ===================================================================
function Write-Step($num, $total, $title) {
    Write-Host ""
    Write-Host "  [$num/$total] $title" -ForegroundColor Cyan
    Write-Host "  -----------------------------------------------------------"
}

function Write-Ok($msg)   { Write-Host "  [OK] $msg" -ForegroundColor Green }
function Write-Warn($msg) { Write-Host "  [WARN] $msg" -ForegroundColor Yellow }
function Write-Fail($msg) { Write-Host "  [X] $msg" -ForegroundColor Red; $script:ErrorCount++ }

function Refresh-Path {
    $machine = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $user    = [Environment]::GetEnvironmentVariable("Path", "User")
    $env:Path = "$machine;$user"
}

function Install-NpmTool {
    param([string]$Name, [string]$Command, [string]$Package, [switch]$AllowScripts)

    Write-Host ""
    Write-Host "  -- $Name --"

    if (Get-Command $Command -ErrorAction SilentlyContinue) {
        $ver = & $Command --version 2>$null
        Write-Host "  $Name already installed: $ver"
        $choice = Read-Host "  [R]einstall / [S]kip (default: S)"
        if ($choice -ne "R") {
            Write-Ok "$Name skipped"
            return "Skipped"
        }
        Write-Host "  Uninstalling $Name..."
        npm uninstall -g $Package 2>&1 | Out-Host
        # Remove leftover binaries from npm global dir
        $npmPrefix = (npm prefix -g 2>$null).Trim()
        if ($npmPrefix) {
            Remove-Item "$npmPrefix\$Command" -Force -ErrorAction SilentlyContinue
            Remove-Item "$npmPrefix\$Command.cmd" -Force -ErrorAction SilentlyContinue
            Remove-Item "$npmPrefix\$Command.ps1" -Force -ErrorAction SilentlyContinue
        }
        npm cache clean --force 2>$null | Out-Null
        Refresh-Path
        Write-Ok "$Name uninstalled"
    }

    for ($i = 1; $i -le $MAX_RETRIES; $i++) {
        Write-Host "  Installing $Name [attempt $i of $MAX_RETRIES]..."
        if ($AllowScripts) {
            npm install -g --allow-scripts=$Package $Package 2>&1 | Out-Host
        } else {
            npm install -g $Package 2>&1 | Out-Host
        }
        if ($LASTEXITCODE -eq 0) {
            Refresh-Path
            Write-Ok "$Name installed"
            return "Installed"
        }
        if ($i -lt $MAX_RETRIES) {
            Write-Warn "Attempt $i failed. Clearing cache and retrying..."
            npm cache clean --force 2>$null | Out-Null
            Start-Sleep -Seconds 2
        }
    }
    Write-Fail "$Name failed after $MAX_RETRIES attempts"
    return "Failed"
}

function Install-GitSkill {
    param([string]$Repo, [string]$TargetDir)

    $parent = Split-Path $TargetDir -Parent
    if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }

    if (Test-Path $TargetDir) {
        Write-Host "  Already installed at $TargetDir"
        $choice = Read-Host "  [R]einstall / [U]pdate / [S]kip (default: S)"
        switch ($choice) {
            "U" { Push-Location $TargetDir; git pull 2>&1 | Out-Host; Pop-Location; Write-Ok "Updated"; return }
            "R" { Remove-Item $TargetDir -Recurse -Force 2>$null }
            default { Write-Ok "Skipped"; return }
        }
    }

    Write-Host "  Cloning into $TargetDir..."
    git clone $Repo $TargetDir 2>&1 | Out-Host
    if ($LASTEXITCODE -eq 0) { Write-Ok "Installed" } else { Write-Fail "Clone failed" }
}

function Run-ClaudePlugin {
    param([string]$Label, [string[]]$CmdArgs)
    Write-Host "  Installing $Label..."
    & claude @CmdArgs 2>&1 | Out-Host
    if ($LASTEXITCODE -eq 0) { Write-Ok $Label } else { Write-Warn "$Label may have had issues" }
}

function Add-ToUserPath {
    param([string]$NewPath)
    $current = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($current -notlike "*$NewPath*") {
        if ($current -and -not $current.EndsWith(";")) { $current += ";" }
        $current += $NewPath
        [Environment]::SetEnvironmentVariable("Path", $current, "User")
        Write-Ok "Added to User PATH: $NewPath"
    } else {
        Write-Ok "Already in PATH: $NewPath"
    }
}

function Add-ToSystemPath {
    param([string]$NewPath)
    try {
        $current = [Environment]::GetEnvironmentVariable("Path", "Machine")
        if ($current -notlike "*$NewPath*") {
            if ($current -and -not $current.EndsWith(";")) { $current += ";" }
            $current += $NewPath
            [Environment]::SetEnvironmentVariable("Path", $current, "Machine")
            $env:PATH += ";$NewPath"
            Write-Ok "Added to System PATH: $NewPath"
        } else {
            Write-Ok "Already in System PATH: $NewPath"
        }
    } catch {
        Write-Warn "Cannot modify System PATH (needs admin). Adding to User PATH instead..."
        Add-ToUserPath $NewPath
    }
}

# Download a file with TLS bypass, timeout, and retries
function Download-WithRetry {
    param([string]$Url, [string]$OutPath, [int]$TimeoutMs = 120000, [int]$Retries = 3)
    try {
        Add-Type @"
using System.Net;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
public class GlobalTlsBypass {
    public static void Enable() {
        ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12 | SecurityProtocolType.Tls11 | SecurityProtocolType.Tls;
    }
}
"@
    } catch {}
    [GlobalTlsBypass]::Enable()

    for ($i = 1; $i -le $Retries; $i++) {
        try {
            Write-Host "  Download attempt $i of $Retries..."
            $wc = New-Object System.Net.WebClient
            # WebClient doesn't have a timeout property; use HttpWebRequest for timeout control
            $uri = New-Object System.Uri($Url)
            $request = [System.Net.HttpWebRequest]::Create($uri)
            $request.Timeout = $TimeoutMs
            $request.ReadWriteTimeout = $TimeoutMs
            $request.AllowAutoRedirect = $true
            $request.UserAgent = "PowerShell/HackathonSetup"
            $response = $request.GetResponse()
            $stream = $response.GetResponseStream()
            $fileStream = [System.IO.File]::Create($OutPath)
            $stream.CopyTo($fileStream)
            $fileStream.Close()
            $stream.Close()
            $response.Close()
            Write-Host "  Download complete."
            return $true
        } catch {
            Write-Warn "Attempt $i failed: $($_.Exception.Message)"
            if ($i -lt $Retries) {
                Write-Host "  Retrying in 5 seconds..."
                Start-Sleep -Seconds 5
            }
        }
    }
    Write-Fail "Download failed after $Retries attempts: $Url"
    return $false
}

function ConvertTo-Hashtable($obj) {
    if ($null -eq $obj) { return @{} }
    $ht = @{}
    foreach ($prop in $obj.PSObject.Properties) { $ht[$prop.Name] = $prop.Value }
    return $ht
}

# ===================================================================
# OPTION 1: Dev Tools Setup
# ===================================================================
function Invoke-ToolSetup {
    Write-Host ""
    Write-Host "  =========================================================" -ForegroundColor Cyan
    Write-Host "       DEV TOOLS SETUP                                     " -ForegroundColor Cyan
    Write-Host "  =========================================================" -ForegroundColor Cyan

    $TOTAL = 9

    # ── [1] Bun ──────────────────────────────────────────────────
    Write-Step 1 $TOTAL "Installing Bun"

    $Tool_Bun = "Skipped"

    # Helper: install Bun with TLS bypass, timeout, and retries
    function Install-Bun {
        $bunDir = "$env:USERPROFILE\.bun\bin"
        New-Item -ItemType Directory -Force -Path $bunDir | Out-Null
        $zipPath = "$bunDir\bun.zip"
        Write-Host "  Downloading Bun (TLS bypass, 120s timeout)..."
        $ok = Download-WithRetry -Url "https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip" -OutPath $zipPath -TimeoutMs 120000 -Retries 3
        if (-not $ok -or -not (Test-Path $zipPath)) {
            Write-Fail "Bun download failed"
            return
        }
        Write-Host "  Extracting..."
        Expand-Archive -Path $zipPath -DestinationPath $bunDir -Force
        Get-ChildItem "$bunDir\bun-windows-x64\*" | Move-Item -Destination $bunDir -Force
        Remove-Item "$bunDir\bun-windows-x64" -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item $zipPath -Force
        if ($env:PATH -notlike "*\.bun\bin*") {
            $env:PATH = "$bunDir;$env:PATH"
        }
        Write-Ok "Bun downloaded and extracted"
    }

    if (Get-Command bun -ErrorAction SilentlyContinue) {
        $bunVer = bun --version 2>$null
        Write-Host "  Bun already installed: $bunVer"
        $choice = Read-Host "  [R]einstall / [S]kip (default: S)"
        if ($choice -ne "R") {
            Write-Ok "Bun skipped"
        } else {
            Install-Bun
            $bunBinDir = "$env:USERPROFILE\.bun\bin"
            Add-ToUserPath $bunBinDir
            Refresh-Path
            if ($env:PATH -notlike "*\.bun\bin*") { $env:PATH = "$bunBinDir;$env:PATH" }
            if (Get-Command bun -ErrorAction SilentlyContinue) { $Tool_Bun = "Installed"; Write-Ok "Bun reinstalled: $(bun --version 2>$null)" } else { Write-Fail "Bun reinstall failed"; $Tool_Bun = "Failed" }
        }
    } else {
        Write-Host "  Installing Bun..."
        Install-Bun
        # Persist .bun\bin to User PATH and ensure it's in current session
        $bunBinDir = "$env:USERPROFILE\.bun\bin"
        Add-ToUserPath $bunBinDir
        Refresh-Path
        if ($env:PATH -notlike "*\.bun\bin*") { $env:PATH = "$bunBinDir;$env:PATH" }
        if (Get-Command bun -ErrorAction SilentlyContinue) { $Tool_Bun = "Installed"; Write-Ok "Bun installed: $(bun --version 2>$null)" } else { Write-Fail "Bun install failed"; $Tool_Bun = "Failed" }
    }

    # ── [2] Prerequisites ────────────────────────────────────────
    Write-Step 2 $TOTAL "Checking Prerequisites"

    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force -ErrorAction SilentlyContinue
    Write-Ok "PowerShell execution policy: RemoteSigned (CurrentUser)"

    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        Write-Fail "Node.js not found. Install from https://nodejs.org"
        Write-Host "  Cannot continue without Node.js. Exiting." -ForegroundColor Red
        Read-Host "  Press Enter to return to menu"; return
    }
    Write-Ok "Node.js $(node --version 2>$null)"

    if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
        Write-Fail "npm not found."
        Read-Host "  Press Enter to return to menu"; return
    }
    Write-Ok "npm v$(npm --version 2>$null)"

    npm config set strict-ssl false 2>$null | Out-Null
    npm config set registry https://registry.npmjs.org/ 2>$null | Out-Null
    $env:NODE_TLS_REJECT_UNAUTHORIZED = "0"
    Write-Ok "npm SSL strict mode disabled (corporate proxy fix)"

    if (Get-Command python -ErrorAction SilentlyContinue) {
        Write-Ok (python --version 2>$null)
    } else { Write-Warn "Python not found - optional" }

    if (Get-Command curl.exe -ErrorAction SilentlyContinue) {
        Write-Ok "curl found"; $script:NoCurl = $false
    } else {
        Write-Warn "curl not found - API validation will be skipped"; $script:NoCurl = $true
    }

    $script:wslOk = $false
    try { wsl --status 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $script:wslOk = $true } } catch {}
    if ($script:wslOk) {
        Write-Ok "WSL available"
    } else {
        Write-Host "  WSL not found. Installing (requires admin)..."
        try {
            wsl --install --no-distribution 2>&1 | Out-Host
            if ($LASTEXITCODE -eq 0) {
                $script:wslOk = $true
                Write-Ok "WSL installed (reboot may be required to complete setup)"
            } else {
                # Fallback: enable WSL feature directly
                Write-Host "  Trying DISM fallback..."
                dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart 2>&1 | Out-Host
                dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart 2>&1 | Out-Host
                Write-Ok "WSL features enabled (reboot required to complete)"
                $script:wslOk = $true
            }
        } catch {
            Write-Warn "WSL install failed: $($_.Exception.Message). Install manually: wsl --install"
        }
    }

    # ── [3] Git ──────────────────────────────────────────────────
    Write-Step 3 $TOTAL "Install Git + Configure User"

    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        Write-Warn "Git not found. Attempting to install..."
        $gitInstalled = $false

        # Method 1: Try winget
        if (Get-Command winget -ErrorAction SilentlyContinue) {
            Write-Host "  Trying winget..."
            winget install -e --id Git.Git --accept-source-agreements --accept-package-agreements 2>&1 | Out-Host
            Refresh-Path
            if (Get-Command git -ErrorAction SilentlyContinue) { $gitInstalled = $true }
        }

        # Method 2: Direct download with TLS bypass
        if (-not $gitInstalled) {
            Write-Host "  Winget failed. Trying direct download (TLS bypass)..."
            $gitInstaller = "$env:TEMP\git-installer.exe"
            $ok = Download-WithRetry -Url "https://github.com/git-for-windows/git/releases/latest/download/Git-2.47.1.2-64-bit.exe" -OutPath $gitInstaller -TimeoutMs 180000 -Retries 3
            if ($ok -and (Test-Path $gitInstaller)) {
                Write-Host "  Running Git installer (silent)..."
                Start-Process -FilePath $gitInstaller -ArgumentList "/VERYSILENT /NORESTART /NOCANCEL /SP- /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS" -Wait -NoNewWindow
                Remove-Item $gitInstaller -Force -ErrorAction SilentlyContinue
                Refresh-Path
                # Add Git to PATH if not found
                $gitPath = "C:\Program Files\Git\cmd"
                if ((Test-Path "$gitPath\git.exe") -and ($env:PATH -notlike "*$gitPath*")) { $env:PATH += ";$gitPath" }
                if (Get-Command git -ErrorAction SilentlyContinue) { $gitInstalled = $true }
            }
        }

        if (-not $gitInstalled) {
            $gitPath = "C:\Program Files\Git\cmd"
            if (Test-Path "$gitPath\git.exe") { $env:Path += ";$gitPath" }
            else {
                Write-Fail "Git install failed. Install manually from https://git-scm.com/download/win"
                Read-Host "  Press Enter to return to menu"; return
            }
        }
    }
    Write-Ok (git --version 2>$null)

    git config --global http.sslVerify false 2>$null
    Write-Ok "Git SSL verify disabled (corporate proxy fix)"

    $existingName  = git config --global user.name 2>$null
    $existingEmail = git config --global user.email 2>$null
    $configureGit = $true
    if ($existingName -and $existingEmail) {
        Write-Host "  Current git user: $existingName <$existingEmail>"
        $change = Read-Host "  Change git user config? [Y/N] (default: N)"
        if ($change -ne "Y") { Write-Ok "Keeping existing git user config"; $configureGit = $false }
    }
    if ($configureGit) {
        $GIT_USERNAME = Read-Host "  Enter Git username"
        $GIT_EMAIL    = Read-Host "  Enter Git email"
        if ($GIT_USERNAME -and $GIT_EMAIL) {
            git config --global user.name $GIT_USERNAME
            git config --global user.email $GIT_EMAIL
            Write-Ok "Git configured: $GIT_USERNAME <$GIT_EMAIL>"
        } else { Write-Warn "Skipped - username or email was empty" }
    }

    # ── [4] Podman CLI ──────────────────────────────────────────
    Write-Step 4 $TOTAL "Installing Podman CLI"

    $Tool_Podman = "Skipped"
    $podmanMsiUrl = "https://github.com/containers/podman/releases/download/v6.1.0/podman-installer-windows-amd64.msi"

    if (Get-Command podman -ErrorAction SilentlyContinue) {
        $podmanVer = podman --version 2>$null
        Write-Host "  Podman already installed: $podmanVer"
        $choice = Read-Host "  [R]einstall / [S]kip (default: S)"
        if ($choice -ne "R") {
            Write-Ok "Podman skipped"
        } else {
            Write-Host "  Uninstalling Podman..."
            # Stop machine if running
            podman machine stop 2>$null | Out-Null
            podman machine rm -f podman-machine-default 2>$null | Out-Null
            # Uninstall via winget or wmic
            if (Get-Command winget -ErrorAction SilentlyContinue) {
                winget uninstall --id "RedHat.Podman" --silent 2>&1 | Out-Host
            } else {
                $uninstall = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" 2>$null |
                    Where-Object { $_.DisplayName -match "Podman" }
                if ($uninstall) {
                    & $uninstall.UninstallString /S 2>$null | Out-Null
                }
            }
            # Clean leftover dirs
            Remove-Item "$env:USERPROFILE\.local\share\containers" -Recurse -Force -ErrorAction SilentlyContinue
            Remove-Item "$env:USERPROFILE\.config\containers" -Recurse -Force -ErrorAction SilentlyContinue
            Refresh-Path
            Write-Ok "Podman uninstalled"

            $installerPath = "$env:TEMP\podman-installer.msi"
            $ok = Download-WithRetry -Url $podmanMsiUrl -OutPath $installerPath -TimeoutMs 180000 -Retries 3
            if ($ok -and (Test-Path $installerPath)) {
                Write-Host "  Running Podman MSI installer (silent)..."
                Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$installerPath`" /qn /norestart" -Wait -NoNewWindow
                Remove-Item $installerPath -Force -ErrorAction SilentlyContinue
            }
            Refresh-Path
            @("$env:ProgramFiles\RedHat\Podman", "$env:LOCALAPPDATA\Programs\RedHat\Podman") | ForEach-Object {
                if ((Test-Path "$_\podman.exe") -and ($env:PATH -notlike "*$_*")) { $env:PATH += ";$_" }
            }
            if (Get-Command podman -ErrorAction SilentlyContinue) { $Tool_Podman = "Installed"; Write-Ok "Podman reinstalled: $(podman --version 2>$null)" }
            else { Write-Fail "Podman reinstall failed"; $Tool_Podman = "Failed" }
        }
    } else {
        Write-Host "  Podman not found. Installing..."
        $installerPath = "$env:TEMP\podman-installer.msi"
        $ok = Download-WithRetry -Url $podmanMsiUrl -OutPath $installerPath -TimeoutMs 180000 -Retries 3
        if ($ok -and (Test-Path $installerPath)) {
            Write-Host "  Running Podman MSI installer (silent)..."
            Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$installerPath`" /qn /norestart" -Wait -NoNewWindow
            Remove-Item $installerPath -Force -ErrorAction SilentlyContinue
        }
        Refresh-Path
        @("$env:ProgramFiles\RedHat\Podman", "$env:LOCALAPPDATA\Programs\RedHat\Podman") | ForEach-Object {
            if ((Test-Path "$_\podman.exe") -and ($env:PATH -notlike "*$_*")) { $env:PATH += ";$_" }
        }
        if (Get-Command podman -ErrorAction SilentlyContinue) { $Tool_Podman = "Installed"; Write-Ok "Podman installed: $(podman --version 2>$null)" }
        else { Write-Fail "Podman install failed"; $Tool_Podman = "Failed" }
    }

    # ── [5] CLI Tools ────────────────────────────────────────────
    Write-Step 5 $TOTAL "Installing CLI Tools"

    $Tool_Claude      = Install-NpmTool -Name "Claude Code"      -Command "claude"       -Package "@anthropic-ai/claude-code" -AllowScripts
    $Tool_Antigravity = Install-NpmTool -Name "Antigravity CLI"  -Command "antigravity"  -Package "antigravity-cli"

    Write-Host ""
    Write-Host "  Checking PATH entries..."
    Add-ToUserPath "$env:APPDATA\npm"
    Add-ToSystemPath "$env:USERPROFILE\.local\bin"
    Refresh-Path

    # ── [6] API Credentials ──────────────────────────────────────
    Write-Step 6 $TOTAL "API Credentials"

    $script:API_KEY = Read-Host "  Enter API Key"
    if (-not $script:API_KEY) {
        Write-Fail "API key is required"
    } else {
        Write-Host "  Default Base URL: $BASE_URL"
        $customUrl = Read-Host "  Press Enter to keep, or type new base URL"
        if ($customUrl) { $script:BASE_URL = $customUrl }
        $keyPreview = $script:API_KEY.Substring(0, [Math]::Min(8, $script:API_KEY.Length))
        Write-Ok "API credentials set (key: $keyPreview..., url: $script:BASE_URL)"
    }

    # ── [7] Validate API ─────────────────────────────────────────
    Write-Step 7 $TOTAL "Validating API Endpoint"

    if (-not $script:API_KEY) {
        Write-Warn "No API key set - skipping validation"
    } elseif ($script:NoCurl) {
        Write-Warn "curl not available - skipping"
    } else {
        Write-Host "  Fetching models from $script:BASE_URL..."
        try {
            $headers = @{
                "Authorization"     = "Bearer $($script:API_KEY)"
                "anthropic-version" = "2023-06-01"
                "x-api-key"         = $script:API_KEY
            }
            [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
            [System.Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }
            $modelsResp = Invoke-RestMethod -Uri "$($script:BASE_URL)/v1/models" -Headers $headers -Method Get -ErrorAction Stop
            Write-Ok "Models fetched successfully"
            Write-Host ""
            Write-Host "  Available Models:"
            Write-Host "  ------------------------------------------------"
            foreach ($m in $modelsResp.data) { Write-Host "    $($m.id)" }
            Write-Host "  ------------------------------------------------"
        } catch {
            Write-Warn "Could not fetch models: $($_.Exception.Message)"
        }

        Write-Host ""
        Write-Host "  Testing chat completions..."
        Write-Host ""
        Write-Host "  Model                Status"
        Write-Host "  -------------------  ------"

        $testModels = @(
            @{ Name = "Opus 4.6";   Id = "genailab-maas-Opus-4.6" },
            @{ Name = "Sonnet 4.6"; Id = "genailab-maas-sonnet-4.6" },
            @{ Name = "Haiku 4.5";  Id = "genailab-maas-Haiku-4.5" }
        )
        foreach ($model in $testModels) {
            $padded = $model.Name.PadRight(19)
            try {
                $body = @{
                    model      = $model.Id
                    max_tokens = 50
                    messages   = @(@{ role = "user"; content = "Say hello in one word." })
                } | ConvertTo-Json -Depth 5
                $resp = Invoke-RestMethod -Uri "$($script:BASE_URL)/v1/messages" -Headers ($headers + @{ "Content-Type" = "application/json" }) -Method Post -Body $body -ErrorAction Stop
                $text = ($resp.content | Where-Object { $_.type -eq "text" } | Select-Object -First 1).text
                Write-Host "  $padded PASS" -ForegroundColor Green
                if ($text) { Write-Host "                          Response: $($text.Substring(0, [Math]::Min(60, $text.Length)))" }
            } catch {
                Write-Host "  $padded FAIL" -ForegroundColor Red
                $script:ErrorCount++
            }
        }
    }

    # ── [8] Claude Code settings.json ────────────────────────────
    Write-Step 8 $TOTAL "Configuring Claude Code settings.json"

    $GH_PAT = Read-Host "  Enter GitHub Personal Access Token (or Enter to skip)"

    if (-not (Test-Path "$env:USERPROFILE\.claude")) { New-Item -ItemType Directory -Path "$env:USERPROFILE\.claude" -Force | Out-Null }

    $settings = @{}
    if (Test-Path $SettingsFile) {
        try { $settings = Get-Content $SettingsFile -Raw | ConvertFrom-Json -ErrorAction Stop } catch {}
    }
    $settings = ConvertTo-Hashtable $settings

    $settings["env"] = [ordered]@{
        ANTHROPIC_BASE_URL             = $script:BASE_URL
        ANTHROPIC_AUTH_TOKEN            = $script:API_KEY
        ANTHROPIC_API_KEY               = ""
        ANTHROPIC_DEFAULT_OPUS_MODEL    = "genailab-maas-Opus-4.6"
        ANTHROPIC_DEFAULT_SONNET_MODEL  = "genailab-maas-sonnet-4.6"
        ANTHROPIC_DEFAULT_HAIKU_MODEL   = "genailab-maas-Haiku-4.5"
    }

    $settings["model"]       = "opus"
    $settings["effortLevel"] = "low"
    $settings["theme"]       = "dark"

    $settings["mcpServers"] = [ordered]@{
        context7 = @{ command = "npx"; args = @("-y", "@upstash/context7-mcp") }
        github   = @{
            command = "npx"; args = @("-y", "@modelcontextprotocol/server-github")
            env = @{ GITHUB_PERSONAL_ACCESS_TOKEN = $GH_PAT }
        }
        supabase = @{
            command = "npx"; args = @("-y", "supabase-mcp-server")
            env = @{ SUPABASE_URL = "http://localhost:3100"; SUPABASE_SERVICE_ROLE_KEY = "your-service-role-key" }
        }
        apidog     = @{ command = "npx"; args = @("-y", "apidog-mcp-server") }
        filesystem = @{ command = "npx"; args = @("-y", "@modelcontextprotocol/server-filesystem", "$env:USERPROFILE\Documents") }
        playwright = @{ command = "npx"; args = @("-y", "@anthropic-ai/mcp-server-playwright") }
        postgresql = @{ command = "npx"; args = @("-y", "@modelcontextprotocol/server-postgres", "postgresql://supabase:postgres@localhost:5432/supabase") }
    }

    $settings | ConvertTo-Json -Depth 10 | Set-Content $SettingsFile -Encoding UTF8
    Write-Ok "settings.json updated"
    Write-Host "      - env: ANTHROPIC_BASE_URL, AUTH_TOKEN, model IDs"
    Write-Host "      - model: opus, effortLevel: low, theme: dark"
    Write-Host "      - 7 MCP servers: context7, github, supabase, apidog,"
    Write-Host "        filesystem, playwright, postgresql"

    # ── [9] Skills & Plugins ─────────────────────────────────────
    Write-Step 9 $TOTAL "Installing Skills and Plugins"

    $vibesecRepo = "https://github.com/BehiSecc/VibeSec-Skill"

    Write-Host ""
    Write-Host "  -- VibeSec for Claude Code (global) --"
    Install-GitSkill -Repo $vibesecRepo -TargetDir "$env:USERPROFILE\.claude\skills\VibeSec-Skill"

    Write-Host ""
    Write-Host "  -- VibeSec for Antigravity (global) --"
    Install-GitSkill -Repo $vibesecRepo -TargetDir "$env:USERPROFILE\.gemini\antigravity\skills\VibeSec-Skill"

    Write-Host ""
    Write-Host "  -----------------------------------------------------------"
    Write-Host "  Installing Claude Code plugins..."
    Write-Host "  -----------------------------------------------------------"

    if (Get-Command claude -ErrorAction SilentlyContinue) {
        Write-Host ""
        Write-Host "  -- Registering plugin marketplaces --"
        Run-ClaudePlugin "Superpowers marketplace" -CmdArgs @("plugin", "marketplace", "add", "obra/superpowers-marketplace")

        Write-Host ""
        Write-Host "  -- Installing plugins from official marketplace --"
        Run-ClaudePlugin "Superpowers (official)" -CmdArgs @("plugin", "install", "superpowers@claude-plugins-official")
        Run-ClaudePlugin "Skill Creator"          -CmdArgs @("plugin", "install", "skill-creator@claude-plugins-official")
        Run-ClaudePlugin "Frontend Design"        -CmdArgs @("plugin", "install", "frontend-design@claude-plugins-official")

        Write-Host ""
        Write-Host "  -- Installing plugins from custom marketplaces --"
        Run-ClaudePlugin "Superpowers (superpowers)" -CmdArgs @("plugin", "install", "superpowers@superpowers-marketplace")

        Write-Host ""
        Write-Host "  -- Installing Get Shit Done --"
        npx --yes get-shit-done-cc --claude --global 2>&1 | Out-Host
        if ($LASTEXITCODE -eq 0) { Write-Ok "Get Shit Done installed" } else { Write-Warn "Get Shit Done may have had issues" }
    } else {
        Write-Warn "Claude Code CLI not found - skipping plugins"
    }

    Write-Host ""
    Write-Host "  -----------------------------------------------------------"
    Write-Host "  Installing Antigravity plugins..."
    Write-Host "  -----------------------------------------------------------"

    $agyCmd = $null
    if (Get-Command agy -ErrorAction SilentlyContinue) { $agyCmd = "agy" }
    elseif (Get-Command antigravity -ErrorAction SilentlyContinue) { $agyCmd = "antigravity" }

    if ($agyCmd) {
        Write-Host "  -- Superpowers for Antigravity --"
        & $agyCmd plugin install https://github.com/obra/superpowers 2>&1 | Out-Host
        if ($LASTEXITCODE -eq 0) { Write-Ok "Superpowers installed for Antigravity" } else { Write-Warn "May have had issues" }

        Write-Host ""
        Write-Host "  -- Get Shit Done for Antigravity --"
        npx --yes get-shit-done-cc --antigravity --global 2>&1 | Out-Host
        if ($LASTEXITCODE -eq 0) { Write-Ok "Get Shit Done installed for Antigravity" } else { Write-Warn "Get Shit Done for Antigravity may have had issues" }
    } else {
        Write-Warn "Antigravity CLI not found - skipping"
    }

    # ── Summary ──────────────────────────────────────────────────
    Write-Host ""
    Write-Host "  =========================================================" -ForegroundColor Cyan
    Write-Host "       DEV TOOLS SETUP - COMPLETE                          " -ForegroundColor Cyan
    Write-Host "  =========================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  CLI TOOLS:"
    Write-Host "    Bun               : $Tool_Bun"
    Write-Host "    Podman            : $Tool_Podman"
    Write-Host "    Claude Code       : $Tool_Claude"
    Write-Host "    Antigravity CLI   : $Tool_Antigravity"
    Write-Host ""
    Write-Host "  GIT:"
    $gitUser  = git config --global user.name 2>$null
    $gitEmail = git config --global user.email 2>$null
    Write-Host "    User              : $gitUser `<$gitEmail`>"
    Write-Host ""
    if ($script:API_KEY) {
        Write-Host "  API:"
        Write-Host "    Key               : $($script:API_KEY.Substring(0,8))..."
        Write-Host "    Base URL          : $script:BASE_URL"
    } else {
        Write-Host "  API:                 Not configured"
    }
    Write-Host ""
    Write-Host "  MCP SERVERS:           7 configured"
    Write-Host "  SETTINGS FILE:         $SettingsFile"
    Write-Host ""
    Write-Host "  Plugins: superpowers, skill-creator, frontend-design, get-shit-done"
    Write-Host ""

    if ($ErrorCount -gt 0) {
        Write-Host "  [WARN] $ErrorCount error(s) occurred." -ForegroundColor Yellow
    } else {
        Write-Ok "All steps completed successfully!"
    }
}

# ===================================================================
# OPTION 2: Podman / LiteLLM + Langfuse Setup
# ===================================================================
function Invoke-PodmanSetup {
    Write-Host ""
    Write-Host "  +==================================================+" -ForegroundColor Magenta
    Write-Host "  |   LITELLM + LANGFUSE PODMAN SETUP               |" -ForegroundColor Magenta
    Write-Host "  |   Corporate-friendly - TLS-skip - Auto-config   |" -ForegroundColor Magenta
    Write-Host "  +==================================================+" -ForegroundColor Magenta

    Set-Location $ScriptDir
    $TOTAL = 8

    # ── [1] Configuration ────────────────────────────────────────
    Write-Step 1 $TOTAL "Configuration"

    $PodmanBaseUrl = Read-Host "  Enter your LLM API Base URL (default: $BASE_URL)"
    if (-not $PodmanBaseUrl) { $PodmanBaseUrl = $BASE_URL }
    $PodmanBaseUrl = $PodmanBaseUrl.TrimEnd('/')

    $PodmanApiKey = Read-Host "  Enter your API Key"
    if (-not $PodmanApiKey) {
        Write-Fail "API key is required"
        Read-Host "  Press Enter to return to menu"; return
    }

    $MasterKey      = "sk-nexus!123"
    $UiUser         = "admin"
    $UiPass         = "nexus!123"
    $SaltKey        = "4e657572616c4e6578757353616c7432303236303030303030303030303030303030"
    $EncryptionKey  = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    $DbPass         = "nexus!123"
    $DbPassEncoded  = $DbPass -replace '!', '%21'

    Write-Ok "Base URL  : $PodmanBaseUrl"
    Write-Ok "API Key   : $($PodmanApiKey.Substring(0,6))***"
    Write-Ok "UI Login  : $UiUser / $UiPass"
    Write-Ok "Master Key: $MasterKey"

    # ── [2] Podman Machine ───────────────────────────────────────
    Write-Step 2 $TOTAL "Setting up Podman Machine"

    try {
        $podmanVer = podman --version
        Write-Ok "Podman found: $podmanVer"
    } catch {
        Write-Fail "Podman not installed! Install from: https://github.com/containers/podman/releases/latest"
        Read-Host "  Press Enter to return to menu"; return
    }

    $machineList = podman machine list --format "{{.Name}}" 2>$null
    if ($machineList -match "podman-machine-default") {
        Write-Warn "Podman machine already exists - skipping init"
    } else {
        Write-Host "  Initializing Podman machine..." -ForegroundColor Gray
        podman machine init
        Write-Ok "Machine initialized"
    }

    Write-Host "  Setting rootful mode..." -ForegroundColor Gray
    podman machine set --rootful 2>$null
    Write-Ok "Rootful mode set"

    $machineInfo = podman machine list --format "{{.LastUp}}" 2>$null
    if ($machineInfo -match "Currently running") {
        Write-Warn "Machine already running"
    } else {
        Write-Host "  Starting Podman machine..." -ForegroundColor Gray
        podman machine start
        Write-Ok "Machine started"
    }

    # ── [3] Pull Images ──────────────────────────────────────────
    Write-Step 3 $TOTAL "Pulling container images (TLS verify disabled)"

    $images = @(
        "ghcr.io/berriai/litellm:main-latest",
        "ghcr.io/langfuse/langfuse:3",
        "ghcr.io/langfuse/langfuse-worker:3",
        "postgres:16-alpine",
        "redis:7",
        "minio/minio:latest",
        "minio/mc:latest",
        "clickhouse/clickhouse-server:latest"
    )

    foreach ($img in $images) {
        $shortName = $img.Split('/')[-1]
        Write-Host "  Pulling $shortName ..." -ForegroundColor Gray -NoNewline
        podman pull --tls-verify=false $img 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host " OK" -ForegroundColor Green
        } else {
            Write-Host " WARN (may already exist locally)" -ForegroundColor Yellow
        }
    }
    Write-Ok "All images pulled"

    # ── [4] Generate init-db.sql ─────────────────────────────────
    Write-Step 4 $TOTAL "Generating init-db.sql"

    Set-Content -Path "$ScriptDir\init-db.sql" -Value "CREATE DATABASE litellm;" -Encoding utf8
    Write-Ok "init-db.sql created"

    # ── [5] Fetch models & generate litellm_config.yaml ──────────
    Write-Step 5 $TOTAL "Fetching models from $PodmanBaseUrl"

    try {
        $modelsJson = wsl -d podman-machine-default -- curl -sk "$PodmanBaseUrl/v1/models" -H "Authorization: Bearer $PodmanApiKey" 2>$null
        $models = ($modelsJson | ConvertFrom-Json).data
        Write-Ok "Found $($models.Count) models"
    } catch {
        Write-Fail "Could not fetch models. Check your Base URL and API Key."
        Write-Host "  Error: $_" -ForegroundColor Red
        Read-Host "  Press Enter to return to menu"; return
    }

    $yaml = @"
general_settings:
  master_key: $MasterKey

litellm_settings:
  drop_params: true
  ssl_verify: false

model_list:
"@

    foreach ($m in $models) {
        $yaml += @"

  - model_name: $($m.id)
    litellm_params:
      model: openai/$($m.id)
      api_base: $PodmanBaseUrl/v1
      api_key: $PodmanApiKey
"@
        $hasInput = $null -ne $m.max_input_tokens -and $m.max_input_tokens -gt 0
        $hasOutput = $null -ne $m.max_output_tokens -and $m.max_output_tokens -gt 0
        if ($hasInput -or $hasOutput) {
            $yaml += "`n      model_info:"
            if ($hasInput)  { $yaml += "`n        max_input_tokens: $($m.max_input_tokens)" }
            if ($hasOutput) { $yaml += "`n        max_output_tokens: $($m.max_output_tokens)" }
        }
    }

    Set-Content -Path "$ScriptDir\litellm_config.yaml" -Value $yaml -Encoding utf8
    Write-Ok "litellm_config.yaml created with $($models.Count) models"

    # ── [6] Generate docker-compose.yml ──────────────────────────
    Write-Step 6 $TOTAL "Generating docker-compose.yml"

    $composeContent = @"
services:
  # -------------------------------------------------------------
  # LiteLLM Proxy (Router & Gateway)
  # -------------------------------------------------------------
  litellm:
    image: ghcr.io/berriai/litellm:main-latest
    container_name: litellm_proxy
    restart: unless-stopped
    ports:
      - "4000:4000"
    environment:
      DATABASE_URL: "postgresql://admin:${DbPassEncoded}@db:5432/litellm"
      STORE_MODEL_IN_DB: "True"
      LITELLM_MASTER_KEY: "$MasterKey"
      LITELLM_SALT_KEY: "$SaltKey"
      UI_USERNAME: "$UiUser"
      UI_PASSWORD: "$UiPass"
      SSL_VERIFY: "false"
      REQUESTS_CA_BUNDLE: ""
      CURL_CA_BUNDLE: ""
      LITELLM_SUCCESS_CALLBACKS: '["langfuse"]'
      LITELLM_FAILURE_CALLBACKS: '["langfuse"]'
      LANGFUSE_HOST: "http://langfuse-server:3000"
      LANGFUSE_SECRET_KEY: "REPLACE_AFTER_LANGFUSE_SETUP"
      LANGFUSE_PUBLIC_KEY: "REPLACE_AFTER_LANGFUSE_SETUP"
    volumes:
      - ./litellm_config.yaml:/app/config.yaml:ro
    command:
      - "--config"
      - "/app/config.yaml"
      - "--host"
      - "0.0.0.0"
      - "--port"
      - "4000"
    depends_on:
      db:
        condition: service_healthy
      langfuse-server:
        condition: service_started

  # -------------------------------------------------------------
  # Langfuse Server & Worker
  # -------------------------------------------------------------
  langfuse-server:
    image: ghcr.io/langfuse/langfuse:3
    container_name: langfuse_web
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
      clickhouse:
        condition: service_healthy
      redis:
        condition: service_healthy
      minio:
        condition: service_healthy
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: "postgresql://admin:${DbPassEncoded}@db:5432/langfuse"
      DIRECT_URL: "postgresql://admin:${DbPassEncoded}@db:5432/langfuse"
      CLICKHOUSE_URL: "http://clickhouse:8123"
      CLICKHOUSE_MIGRATION_URL: "clickhouse://default:${DbPass}@clickhouse:9000/default"
      CLICKHOUSE_USER: "default"
      CLICKHOUSE_PASSWORD: "$DbPass"
      CLICKHOUSE_CLUSTER_ENABLED: "false"
      REDIS_URL: "redis://redis:6379"
      LANGFUSE_S3_EVENT_UPLOAD_BUCKET: "langfuse"
      LANGFUSE_S3_EVENT_UPLOAD_REGION: "us-east-1"
      LANGFUSE_S3_EVENT_UPLOAD_ENDPOINT: "http://minio:9000"
      LANGFUSE_S3_EVENT_UPLOAD_ACCESS_KEY_ID: "admin"
      LANGFUSE_S3_EVENT_UPLOAD_SECRET_ACCESS_KEY: "$DbPass"
      LANGFUSE_S3_EVENT_UPLOAD_FORCE_PATH_STYLE: "true"
      AUTH_DISABLE_SIGNUP: "false"
      AUTH_DISABLE_USERNAME_PASSWORD: "false"
      NEXTAUTH_URL: "http://localhost:3000"
      NEXTAUTH_SECRET: "$SaltKey"
      SALT: "$SaltKey"
      ENCRYPTION_KEY: "$EncryptionKey"
      TELEMETRY_ENABLED: "false"

  langfuse-worker:
    image: ghcr.io/langfuse/langfuse-worker:3
    container_name: langfuse_worker
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
      clickhouse:
        condition: service_healthy
      redis:
        condition: service_healthy
      minio:
        condition: service_healthy
    environment:
      DATABASE_URL: "postgresql://admin:${DbPassEncoded}@db:5432/langfuse"
      CLICKHOUSE_URL: "http://clickhouse:8123"
      CLICKHOUSE_MIGRATION_URL: "clickhouse://default:${DbPass}@clickhouse:9000/default"
      CLICKHOUSE_USER: "default"
      CLICKHOUSE_PASSWORD: "$DbPass"
      CLICKHOUSE_CLUSTER_ENABLED: "false"
      REDIS_URL: "redis://redis:6379"
      LANGFUSE_S3_EVENT_UPLOAD_BUCKET: "langfuse"
      LANGFUSE_S3_EVENT_UPLOAD_REGION: "us-east-1"
      LANGFUSE_S3_EVENT_UPLOAD_ENDPOINT: "http://minio:9000"
      LANGFUSE_S3_EVENT_UPLOAD_ACCESS_KEY_ID: "admin"
      LANGFUSE_S3_EVENT_UPLOAD_SECRET_ACCESS_KEY: "$DbPass"
      LANGFUSE_S3_EVENT_UPLOAD_FORCE_PATH_STYLE: "true"
      SALT: "$SaltKey"
      ENCRYPTION_KEY: "$EncryptionKey"
      TELEMETRY_ENABLED: "false"

  # -------------------------------------------------------------
  # Shared PostgreSQL
  # -------------------------------------------------------------
  db:
    image: postgres:16-alpine
    container_name: shared_db
    restart: unless-stopped
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: $DbPass
      POSTGRES_DB: langfuse
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init-db.sql:/docker-entrypoint-initdb.d/init-db.sql:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d langfuse"]
      interval: 5s
      timeout: 5s
      retries: 5

  # -------------------------------------------------------------
  # ClickHouse, Redis, and MinIO
  # -------------------------------------------------------------
  clickhouse:
    image: clickhouse/clickhouse-server:latest
    container_name: langfuse_clickhouse
    restart: unless-stopped
    environment:
      CLICKHOUSE_DB: default
      CLICKHOUSE_USER: default
      CLICKHOUSE_PASSWORD: $DbPass
      CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT: 1
    volumes:
      - clickhouse_data:/var/lib/clickhouse
    healthcheck:
      test: ["CMD-SHELL", "wget -q --spider http://127.0.0.1:8123/ping || exit 1"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7
    container_name: langfuse_redis
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5

  minio:
    image: minio/minio:latest
    container_name: langfuse_minio
    restart: unless-stopped
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: admin
      MINIO_ROOT_PASSWORD: $DbPass
    volumes:
      - minio_data:/data
    healthcheck:
      test: ["CMD", "mc", "ready", "local"]
      interval: 5s
      timeout: 5s
      retries: 5

  minio-create-bucket:
    image: minio/mc:latest
    container_name: langfuse_minio_init
    depends_on:
      minio:
        condition: service_healthy
    entrypoint: >
      /bin/sh -c "
      /usr/bin/mc alias set myminio http://minio:9000 admin $DbPass;
      /usr/bin/mc mb --ignore-existing myminio/langfuse;
      exit 0;
      "

volumes:
  pgdata:
  clickhouse_data:
  minio_data:
"@

    Set-Content -Path "$ScriptDir\docker-compose.yml" -Value $composeContent -Encoding utf8
    Write-Ok "docker-compose.yml created"

    # ── [7] Port Forwarding ──────────────────────────────────────
    Write-Step 7 $TOTAL "Setting up port forwarding (WSL -> Windows)"

    try {
        $wslIpRaw = wsl -d podman-machine-default -- ip -4 addr show eth0 2>$null
        $wslIp = ($wslIpRaw | Select-String -Pattern 'inet (\d+\.\d+\.\d+\.\d+)').Matches.Groups[1].Value

        if ($wslIp) {
            Write-Ok "WSL IP: $wslIp"
            Write-Host ""
            Write-Host "  [!] Port forwarding requires Admin PowerShell." -ForegroundColor Yellow
            Write-Host "  Run this in an elevated (Admin) PowerShell:" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "  netsh interface portproxy add v4tov4 listenport=4000 listenaddress=127.0.0.1 connectport=4000 connectaddress=$wslIp" -ForegroundColor White
            Write-Host "  netsh interface portproxy add v4tov4 listenport=3000 listenaddress=127.0.0.1 connectport=3000 connectaddress=$wslIp" -ForegroundColor White
            Write-Host ""

            $portFwdScript = @"
# Run this as Administrator to enable localhost access
netsh interface portproxy add v4tov4 listenport=4000 listenaddress=127.0.0.1 connectport=4000 connectaddress=$wslIp
netsh interface portproxy add v4tov4 listenport=3000 listenaddress=127.0.0.1 connectport=3000 connectaddress=$wslIp
Write-Host "Port forwarding configured! Access:"
Write-Host "  LiteLLM  : http://localhost:4000/ui"
Write-Host "  Langfuse : http://localhost:3000"
"@
            Set-Content -Path "$ScriptDir\enable-ports.ps1" -Value $portFwdScript -Encoding utf8
            Write-Ok "Saved to enable-ports.ps1 (run as Admin)"
        }
    } catch {
        Write-Warn "Could not detect WSL IP - set up port forwarding manually"
    }

    # ── [8] Start Services ───────────────────────────────────────
    Write-Step 8 $TOTAL "Starting all services"

    podman compose up -d
    if ($LASTEXITCODE -eq 0) {
        Write-Ok "All services started!"
    } else {
        Write-Fail "Compose failed - check errors above"
        Read-Host "  Press Enter to return to menu"; return
    }

    Write-Host "  Waiting for services to become healthy (20s)..." -ForegroundColor Gray
    Start-Sleep -Seconds 20

    # ── Summary ──────────────────────────────────────────────────
    Write-Host ""
    Write-Host "  +==================================================+" -ForegroundColor Green
    Write-Host "  |   PODMAN SETUP COMPLETE!                        |" -ForegroundColor Green
    Write-Host "  +==================================================+" -ForegroundColor Green
    Write-Host "  |                                                  |" -ForegroundColor Green
    Write-Host "  |   LiteLLM UI : http://localhost:4000/ui          |" -ForegroundColor Green
    Write-Host "  |   Langfuse   : http://localhost:3000             |" -ForegroundColor Green
    Write-Host "  |                                                  |" -ForegroundColor Green
    Write-Host "  |   UI Login   : admin / $UiPass              |" -ForegroundColor Green
    Write-Host "  |   Master Key : $MasterKey                |" -ForegroundColor Green
    Write-Host "  |   Models     : $($models.Count) auto-discovered           |" -ForegroundColor Green
    Write-Host "  |                                                  |" -ForegroundColor Green
    Write-Host "  |   If localhost doesn't work, run as Admin:       |" -ForegroundColor Yellow
    Write-Host "  |      .\enable-ports.ps1                          |" -ForegroundColor Yellow
    Write-Host "  |                                                  |" -ForegroundColor Green
    Write-Host "  |   Next: Sign into Langfuse, create API keys,    |" -ForegroundColor Green
    Write-Host "  |   then update LANGFUSE_SECRET/PUBLIC_KEY in      |" -ForegroundColor Green
    Write-Host "  |   docker-compose.yml and restart litellm.        |" -ForegroundColor Green
    Write-Host "  +==================================================+" -ForegroundColor Green
    Write-Host ""

    podman ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
}

# ===================================================================
# OPTION 3: Run Both
# ===================================================================
function Invoke-FullSetup {
    Invoke-ToolSetup
    Write-Host ""
    Write-Host "  =========================================================" -ForegroundColor Yellow
    Write-Host "  Dev tools done. Proceeding to Podman setup..." -ForegroundColor Yellow
    Write-Host "  =========================================================" -ForegroundColor Yellow
    Invoke-PodmanSetup
}

# ===================================================================
# MAIN MENU LOOP
# ===================================================================
$running = $true
while ($running) {
    Clear-Host
    Write-Host ""
    Write-Host "  +======================================================+" -ForegroundColor Cyan
    Write-Host "  |          HACKATHON MASTER SETUP                     |" -ForegroundColor Cyan
    Write-Host "  +======================================================+" -ForegroundColor Cyan
    Write-Host "  |                                                      |" -ForegroundColor Cyan
    Write-Host "  |   [1]  Dev Tools Setup                               |" -ForegroundColor Cyan
    Write-Host "  |        Bun, Node, Git, Claude Code, Antigravity,     |" -ForegroundColor DarkGray
    Write-Host "  |        API keys, settings.json, skills/plugins       |" -ForegroundColor DarkGray
    Write-Host "  |                                                      |" -ForegroundColor Cyan
    Write-Host "  |   [2]  Podman + LiteLLM + Langfuse Setup            |" -ForegroundColor Cyan
    Write-Host "  |        Podman machine, pull images, generate         |" -ForegroundColor DarkGray
    Write-Host "  |        configs, start all containers                 |" -ForegroundColor DarkGray
    Write-Host "  |                                                      |" -ForegroundColor Cyan
    Write-Host "  |   [3]  Full Setup (both 1 + 2)                       |" -ForegroundColor Cyan
    Write-Host "  |                                                      |" -ForegroundColor Cyan
    Write-Host "  |   [Q]  Quit                                          |" -ForegroundColor Cyan
    Write-Host "  |                                                      |" -ForegroundColor Cyan
    Write-Host "  +======================================================+" -ForegroundColor Cyan
    Write-Host ""

    $choice = Read-Host "  Select an option"

    switch ($choice) {
        "1" { Invoke-ToolSetup;  Write-Host ""; Read-Host "  Press Enter to return to menu" }
        "2" { Invoke-PodmanSetup; Write-Host ""; Read-Host "  Press Enter to return to menu" }
        "3" { Invoke-FullSetup;  Write-Host ""; Read-Host "  Press Enter to return to menu" }
        "Q" { $running = $false }
        "q" { $running = $false }
        default { Write-Host "  Invalid option. Try again." -ForegroundColor Red; Start-Sleep 1 }
    }
}

Write-Host ""
Write-Host "  Goodbye! Happy hacking!" -ForegroundColor Cyan
Write-Host ""
