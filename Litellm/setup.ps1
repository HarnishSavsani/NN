#Requires -Version 5.1
# powershell -ExecutionPolicy Bypass -File ./setup.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# ===================================================================
# Config
# ===================================================================
$BASE_URL      = "https://genailab.tcs.in"
$MAX_RETRIES   = 3
$ErrorCount    = 0
$SettingsFile  = "$env:USERPROFILE\.claude\settings.json"
$ServicesDir   = "$env:USERPROFILE\Documents\hackathon-services"

# ===================================================================
# Helper Functions
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
        npm uninstall -g $Package 2>$null | Out-Null
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

# ===================================================================
# Banner
# ===================================================================
Clear-Host
Write-Host ""
Write-Host "  =========================================================" -ForegroundColor Cyan
Write-Host "       HACKATHON MACHINE SETUP SCRIPT (PowerShell)         " -ForegroundColor Cyan
Write-Host "  =========================================================" -ForegroundColor Cyan
Write-Host ""

$TOTAL_STEPS = 10

# ===================================================================
# [1] Install Bun (early - used by other tools)
# ===================================================================
Write-Step 1 $TOTAL_STEPS "Installing Bun"

$Tool_Bun = "Skipped"
if (Get-Command bun -ErrorAction SilentlyContinue) {
    $bunVer = bun --version 2>$null
    Write-Host "  Bun already installed: $bunVer"
    $choice = Read-Host "  [R]einstall / [S]kip (default: S)"
    if ($choice -ne "R") {
        Write-Ok "Bun skipped"
    } else {
        powershell -c "irm bun.sh/install.ps1 | iex" 2>&1 | Out-Host
        Refresh-Path
        if (Get-Command bun -ErrorAction SilentlyContinue) { $Tool_Bun = "Installed"; Write-Ok "Bun reinstalled" } else { Write-Fail "Bun reinstall failed"; $Tool_Bun = "Failed" }
    }
} else {
    Write-Host "  Installing Bun..."
    powershell -c "irm bun.sh/install.ps1 | iex" 2>&1 | Out-Host
    Refresh-Path
    if (Get-Command bun -ErrorAction SilentlyContinue) { $Tool_Bun = "Installed"; Write-Ok "Bun installed" } else { Write-Fail "Bun install failed"; $Tool_Bun = "Failed" }
}

# ===================================================================
# [2] Prerequisites
# ===================================================================
Write-Step 2 $TOTAL_STEPS "Checking Prerequisites"

# PowerShell execution policy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force -ErrorAction SilentlyContinue
Write-Ok "PowerShell execution policy: RemoteSigned (CurrentUser)"

# Node.js
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Fail "Node.js not found. Install from https://nodejs.org"
    Write-Host "  Cannot continue without Node.js. Exiting." -ForegroundColor Red
    Read-Host "  Press Enter to exit"
    exit 1
}
$nodeVer = node --version 2>$null
Write-Ok "Node.js $nodeVer"

# npm
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    Write-Fail "npm not found."
    Read-Host "  Press Enter to exit"
    exit 1
}
$npmVer = npm --version 2>$null
Write-Ok "npm v$npmVer"

# npm SSL fix for corporate proxy
npm config set strict-ssl false 2>$null | Out-Null
npm config set registry https://registry.npmjs.org/ 2>$null | Out-Null
$env:NODE_TLS_REJECT_UNAUTHORIZED = "0"
Write-Ok "npm SSL strict mode disabled (corporate proxy fix)"

# Python (optional)
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pyVer = python --version 2>$null
    Write-Ok $pyVer
} else { Write-Warn "Python not found - optional" }

# curl
if (Get-Command curl.exe -ErrorAction SilentlyContinue) {
    Write-Ok "curl found"
    $NoCurl = $false
} else {
    Write-Warn "curl not found - API validation will be skipped"
    $NoCurl = $true
}

# WSL
$wslOk = $false
try { wsl --status 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $wslOk = $true } } catch {}
if ($wslOk) { Write-Ok "WSL available" } else { Write-Warn "WSL not installed - needed for containers" }

# ===================================================================
# [3] Install Git + Configure User
# ===================================================================
Write-Step 3 $TOTAL_STEPS "Install Git + Configure User"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Warn "Git not found. Attempting to install..."

    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host "  Installing Git via winget..."
        winget install -e --id Git.Git --accept-source-agreements --accept-package-agreements 2>&1 | Out-Host
    }

    Refresh-Path

    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        # Try common install path
        $gitPath = "C:\Program Files\Git\cmd"
        if (Test-Path "$gitPath\git.exe") {
            $env:Path += ";$gitPath"
        } else {
            Write-Fail "Git still not found. Install from https://git-scm.com/download/win"
            Write-Host "  Install Git, then re-run this script."
            Read-Host "  Press Enter to exit"
            exit 1
        }
    }
}

$gitVer = git --version 2>$null
Write-Ok $gitVer

# SSL fix
git config --global http.sslVerify false 2>$null
Write-Ok "Git SSL verify disabled (corporate proxy fix)"

# Configure user
$existingName  = git config --global user.name 2>$null
$existingEmail = git config --global user.email 2>$null

$configureGit = $true
if ($existingName -and $existingEmail) {
    Write-Host "  Current git user: $existingName <$existingEmail>"
    $change = Read-Host "  Change git user config? [Y/N] (default: N)"
    if ($change -ne "Y") {
        Write-Ok "Keeping existing git user config"
        $configureGit = $false
    }
}

if ($configureGit) {
    $GIT_USERNAME = Read-Host "  Enter Git username"
    $GIT_EMAIL    = Read-Host "  Enter Git email"
    if ($GIT_USERNAME -and $GIT_EMAIL) {
        git config --global user.name $GIT_USERNAME
        git config --global user.email $GIT_EMAIL
        Write-Ok "Git configured: $GIT_USERNAME <$GIT_EMAIL>"
    } else {
        Write-Warn "Skipped - username or email was empty"
    }
}

# ===================================================================
# [4] Install CLI Tools
# ===================================================================
Write-Step 4 $TOTAL_STEPS "Installing CLI Tools"

$Tool_Claude      = Install-NpmTool -Name "Claude Code"      -Command "claude"       -Package "@anthropic-ai/claude-code" -AllowScripts
$Tool_Antigravity = Install-NpmTool -Name "Antigravity CLI"  -Command "antigravity"  -Package "antigravity-cli"

# Add paths to User PATH
Write-Host ""
Write-Host "  Checking User PATH..."
Add-ToUserPath "$env:APPDATA\npm"
Add-ToUserPath "$env:USERPROFILE\.local\bin"
Refresh-Path

# ===================================================================
# [5] API Credentials
# ===================================================================
Write-Step 5 $TOTAL_STEPS "API Credentials"

$API_KEY = Read-Host "  Enter API Key"
if (-not $API_KEY) {
    Write-Fail "API key is required"
} else {
    Write-Host "  Default Base URL: $BASE_URL"
    $customUrl = Read-Host "  Press Enter to keep, or type new base URL"
    if ($customUrl) { $BASE_URL = $customUrl }
    $keyPreview = $API_KEY.Substring(0, [Math]::Min(8, $API_KEY.Length))
    Write-Ok "API credentials set (key: $keyPreview..., url: $BASE_URL)"
}

# ===================================================================
# [6] Validate API Endpoint
# ===================================================================
Write-Step 6 $TOTAL_STEPS "Validating API Endpoint"

if (-not $API_KEY) {
    Write-Warn "No API key set - skipping validation"
} elseif ($NoCurl) {
    Write-Warn "curl not available - skipping"
} else {
    # Fetch models
    Write-Host "  Fetching models from $BASE_URL..."
    try {
        $headers = @{
            "Authorization"     = "Bearer $API_KEY"
            "anthropic-version" = "2023-06-01"
            "x-api-key"         = $API_KEY
        }
        # Bypass SSL for corporate proxy + force TLS 1.2
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
        [System.Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }
        $modelsResp = Invoke-RestMethod -Uri "$BASE_URL/v1/models" -Headers $headers -Method Get -ErrorAction Stop
        Write-Ok "Models fetched successfully"
        Write-Host ""
        Write-Host "  Available Models:"
        Write-Host "  ------------------------------------------------"
        foreach ($m in $modelsResp.data) {
            Write-Host "    $($m.id)"
        }
        Write-Host "  ------------------------------------------------"
    } catch {
        Write-Warn "Could not fetch models: $($_.Exception.Message)"
    }

    # Test chat completions
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

            $resp = Invoke-RestMethod -Uri "$BASE_URL/v1/messages" -Headers ($headers + @{ "Content-Type" = "application/json" }) -Method Post -Body $body -ErrorAction Stop
            $text = ($resp.content | Where-Object { $_.type -eq "text" } | Select-Object -First 1).text
            Write-Host "  $padded PASS" -ForegroundColor Green
            if ($text) { Write-Host "                          Response: $($text.Substring(0, [Math]::Min(60, $text.Length)))" }
        } catch {
            Write-Host "  $padded FAIL" -ForegroundColor Red
            $script:ErrorCount++
        }
    }
}

# ===================================================================
# [7] Configure Claude Code settings.json
# ===================================================================
Write-Step 7 $TOTAL_STEPS "Configuring Claude Code settings.json"

$GH_PAT = Read-Host "  Enter GitHub Personal Access Token (or Enter to skip)"

# Ensure directories exist
if (-not (Test-Path "$env:USERPROFILE\.claude")) { New-Item -ItemType Directory -Path "$env:USERPROFILE\.claude" -Force | Out-Null }

# Read existing or start fresh
$settings = @{}
if (Test-Path $SettingsFile) {
    try { $settings = Get-Content $SettingsFile -Raw | ConvertFrom-Json -ErrorAction Stop } catch {}
}

# Convert PSObject to hashtable for easy manipulation
function ConvertTo-Hashtable($obj) {
    if ($null -eq $obj) { return @{} }
    $ht = @{}
    foreach ($prop in $obj.PSObject.Properties) { $ht[$prop.Name] = $prop.Value }
    return $ht
}

$settings = ConvertTo-Hashtable $settings

# Environment variables
$settings["env"] = [ordered]@{
    ANTHROPIC_BASE_URL             = $BASE_URL
    ANTHROPIC_AUTH_TOKEN            = $API_KEY
    ANTHROPIC_API_KEY               = ""
    ANTHROPIC_DEFAULT_OPUS_MODEL    = "genailab-maas-Opus-4.6"
    ANTHROPIC_DEFAULT_SONNET_MODEL  = "genailab-maas-sonnet-4.6"
    ANTHROPIC_DEFAULT_HAIKU_MODEL   = "genailab-maas-Haiku-4.5"
}

# Model and UI settings
$settings["model"]       = "opus"
$settings["effortLevel"] = "low"
$settings["theme"]       = "dark"


# MCP Servers
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

# Write settings.json
$settings | ConvertTo-Json -Depth 10 | Set-Content $SettingsFile -Encoding UTF8
Write-Ok "settings.json updated:"
Write-Host "      - env: ANTHROPIC_BASE_URL, AUTH_TOKEN, model IDs"
Write-Host "      - model: opus, effortLevel: low, theme: dark"
Write-Host "      - 7 MCP servers: context7, github, supabase, apidog,"
Write-Host "        filesystem, playwright, postgresql"

# ===================================================================
# [8] Install Skills and Plugins
# ===================================================================
Write-Step 8 $TOTAL_STEPS "Installing Skills and Plugins"

$vibesecRepo = "https://github.com/BehiSecc/VibeSec-Skill"

# --- Git-cloned skills ---
Write-Host ""
Write-Host "  -- VibeSec for Claude Code (global) --"
Install-GitSkill -Repo $vibesecRepo -TargetDir "$env:USERPROFILE\.claude\skills\VibeSec-Skill"

Write-Host ""
Write-Host "  -- VibeSec for Antigravity (global) --"
Install-GitSkill -Repo $vibesecRepo -TargetDir "$env:USERPROFILE\.gemini\antigravity\skills\VibeSec-Skill"

# --- Claude Code Plugins ---
Write-Host ""
Write-Host "  -----------------------------------------------------------"
Write-Host "  Installing Claude Code plugins..."
Write-Host "  -----------------------------------------------------------"

if (Get-Command claude -ErrorAction SilentlyContinue) {
    # Register marketplaces
    Write-Host ""
    Write-Host "  -- Registering plugin marketplaces --"
    Run-ClaudePlugin "Superpowers marketplace"  -CmdArgs @("plugin", "marketplace", "add", "obra/superpowers-marketplace")

    # Install from official
    Write-Host ""
    Write-Host "  -- Installing plugins from official marketplace --"
    Run-ClaudePlugin "Superpowers (official)" -CmdArgs @("plugin", "install", "superpowers@claude-plugins-official")
    Run-ClaudePlugin "Skill Creator"          -CmdArgs @("plugin", "install", "skill-creator@claude-plugins-official")
    Run-ClaudePlugin "Frontend Design"        -CmdArgs @("plugin", "install", "frontend-design@claude-plugins-official")

    # Install from custom
    Write-Host ""
    Write-Host "  -- Installing plugins from custom marketplaces --"
    Run-ClaudePlugin "Superpowers (superpowers)" -CmdArgs @("plugin", "install", "superpowers@superpowers-marketplace")

    # Get Shit Done
    Write-Host ""
    Write-Host "  -- Installing Get Shit Done --"
    npx --yes get-shit-done-cc --claude --global 2>&1 | Out-Host
    if ($LASTEXITCODE -eq 0) { Write-Ok "Get Shit Done installed" } else { Write-Warn "Get Shit Done may have had issues" }
} else {
    Write-Warn "Claude Code CLI not found - skipping plugins"
}

# --- Antigravity Plugins ---
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
} else {
    Write-Warn "Antigravity CLI not found - skipping"
}

# Summary
Write-Host ""
Write-Host "  -----------------------------------------------------------"
Write-Host "  Skills and Plugins summary:"
Write-Host "  -----------------------------------------------------------"
Write-Host ""
Write-Host "  Git-cloned skills:"
Write-Host "    Claude Code : $env:USERPROFILE\.claude\skills\VibeSec-Skill"
Write-Host "    Antigravity : $env:USERPROFILE\.gemini\antigravity\skills\VibeSec-Skill"
Write-Host ""
Write-Host "  Claude Code plugins: superpowers, skill-creator, frontend-design,"
Write-Host "    get-shit-done"
Write-Host "  Antigravity plugins: superpowers"

# ===================================================================
# [9] Install WSL
# ===================================================================
Write-Step 9 $TOTAL_STEPS "WSL (Windows Subsystem for Linux)"

$wslOk = $false
try { wsl --status 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $wslOk = $true } } catch {}

if ($wslOk) {
    Write-Ok "WSL is already installed"
} else {
    Write-Warn "WSL is not installed."
    $installWsl = Read-Host "  Install WSL now? [Y/N] (default: N)"
    if ($installWsl -eq "Y") {
        Write-Host "  Installing WSL (this may take a few minutes)..."
        wsl --install --no-distribution 2>&1 | Out-Host
        if ($LASTEXITCODE -eq 0) {
            Write-Ok "WSL installed successfully"
            Write-Host ""
            Write-Host "  *** IMPORTANT: A RESTART may be required for WSL to work. ***" -ForegroundColor Yellow
        } else {
            Write-Fail "WSL install failed. Try running as Administrator: wsl --install"
        }
    } else {
        Write-Warn "Skipped WSL install"
    }
}

# ===================================================================
# [10] Start Containers (Supabase + Langfuse)
# ===================================================================
Write-Step 10 $TOTAL_STEPS "Starting Container Services"

$SVC_Supabase = "Skipped"
$SVC_Langfuse = "Skipped"

if (-not (Get-Command podman -ErrorAction SilentlyContinue)) {
    Write-Warn "Podman not installed - skipping containers"
    Write-Host "  Install Podman Desktop manually first."
} else {
    # Verify connection
    podman info 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  Trying to start Podman machine..."
        podman machine start 2>&1 | Out-Host
        podman info 2>$null | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Fail "Cannot connect to Podman"
        }
    }

    if ($LASTEXITCODE -eq 0) {
        # Generate secrets
        $PG_PASSWORD     = "hackpg$(Get-Random)$(Get-Random)"
        $JWT_SECRET      = "hackjwt$(Get-Random)$(Get-Random)$(Get-Random)"
        $ANON_KEY        = "hackanon$(Get-Random)$(Get-Random)$(Get-Random)"
        $SERVICE_ROLE_KEY = "hacksrk$(Get-Random)$(Get-Random)$(Get-Random)"
        $NEXTAUTH_SECRET = "hackna$(Get-Random)$(Get-Random)$(Get-Random)"
        $SALT            = "hacksalt$(Get-Random)$(Get-Random)"

        # -- Supabase --
        Write-Host ""
        Write-Host "  -- Supabase --"
        $supaDir = "$ServicesDir\supabase"
        if (-not (Test-Path $supaDir)) { New-Item -ItemType Directory -Path $supaDir -Force | Out-Null }

        @"
POSTGRES_PASSWORD=$PG_PASSWORD
JWT_SECRET=$JWT_SECRET
ANON_KEY=$ANON_KEY
SERVICE_ROLE_KEY=$SERVICE_ROLE_KEY
"@ | Set-Content "$supaDir\.env" -Encoding UTF8

        @"
version: "3.8"
services:
  supabase-db:
    image: postgres:15-alpine
    restart: unless-stopped
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: supabase
      POSTGRES_PASSWORD: `${POSTGRES_PASSWORD}
      POSTGRES_DB: supabase
    volumes:
      - supabase-db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U supabase"]
      interval: 10s
      timeout: 5s
      retries: 5
  supabase-rest:
    image: postgrest/postgrest:latest
    restart: unless-stopped
    ports:
      - "3100:3000"
    environment:
      PGRST_DB_URI: postgres://supabase:`${POSTGRES_PASSWORD}@supabase-db:5432/supabase
      PGRST_DB_SCHEMAS: public,storage
      PGRST_DB_ANON_ROLE: anon
      PGRST_JWT_SECRET: `${JWT_SECRET}
    depends_on:
      supabase-db:
        condition: service_healthy
  supabase-studio:
    image: supabase/studio:latest
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      STUDIO_PG_META_URL: http://supabase-meta:8080
      SUPABASE_URL: http://supabase-rest:3000
      SUPABASE_REST_URL: http://localhost:3100
      SUPABASE_ANON_KEY: `${ANON_KEY}
      SUPABASE_SERVICE_KEY: `${SERVICE_ROLE_KEY}
  supabase-meta:
    image: supabase/postgres-meta:latest
    restart: unless-stopped
    ports:
      - "8080:8080"
    environment:
      PG_META_PORT: 8080
      PG_META_DB_HOST: supabase-db
      PG_META_DB_PORT: 5432
      PG_META_DB_NAME: supabase
      PG_META_DB_USER: supabase
      PG_META_DB_PASSWORD: `${POSTGRES_PASSWORD}
    depends_on:
      supabase-db:
        condition: service_healthy
volumes:
  supabase-db-data:
"@ | Set-Content "$supaDir\docker-compose.yml" -Encoding UTF8

        for ($i = 1; $i -le $MAX_RETRIES; $i++) {
            Write-Host "  Running podman compose up -d [attempt $i of $MAX_RETRIES]..."
            Push-Location $supaDir
            podman compose up -d 2>&1 | Out-Host
            $composeErr = $LASTEXITCODE
            Pop-Location
            if ($composeErr -eq 0) { $SVC_Supabase = "Running"; Write-Ok "Supabase started: Studio :3000  REST :3100  DB :5432"; break }
            if ($i -lt $MAX_RETRIES) { Write-Warn "Attempt $i failed. Retrying in 3s..."; Start-Sleep 3 }
            else { Write-Fail "Supabase failed after $MAX_RETRIES attempts"; $SVC_Supabase = "Failed" }
        }

        # -- Langfuse --
        Write-Host ""
        Write-Host "  -- Langfuse --"
        $lfDir = "$ServicesDir\langfuse"
        if (-not (Test-Path $lfDir)) { New-Item -ItemType Directory -Path $lfDir -Force | Out-Null }

        @"
NEXTAUTH_SECRET=$NEXTAUTH_SECRET
SALT=$SALT
"@ | Set-Content "$lfDir\.env" -Encoding UTF8

        @"
version: "3.8"
services:
  langfuse-db:
    image: postgres:15-alpine
    restart: unless-stopped
    ports:
      - "5433:5432"
    environment:
      POSTGRES_USER: langfuse
      POSTGRES_PASSWORD: langfuse123
      POSTGRES_DB: langfuse
    volumes:
      - langfuse-db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U langfuse"]
      interval: 10s
      timeout: 5s
      retries: 5
  langfuse:
    image: langfuse/langfuse:latest
    restart: unless-stopped
    ports:
      - "3001:3000"
    environment:
      DATABASE_URL: postgresql://langfuse:langfuse123@langfuse-db:5432/langfuse
      NEXTAUTH_SECRET: `${NEXTAUTH_SECRET}
      NEXTAUTH_URL: http://localhost:3001
      SALT: `${SALT}
    depends_on:
      langfuse-db:
        condition: service_healthy
volumes:
  langfuse-db-data:
"@ | Set-Content "$lfDir\docker-compose.yml" -Encoding UTF8

        for ($i = 1; $i -le $MAX_RETRIES; $i++) {
            Write-Host "  Running podman compose up -d [attempt $i of $MAX_RETRIES]..."
            Push-Location $lfDir
            podman compose up -d 2>&1 | Out-Host
            $composeErr = $LASTEXITCODE
            Pop-Location
            if ($composeErr -eq 0) { $SVC_Langfuse = "Running"; Write-Ok "Langfuse started: http://localhost:3001"; break }
            if ($i -lt $MAX_RETRIES) { Write-Warn "Attempt $i failed. Retrying in 3s..."; Start-Sleep 3 }
            else { Write-Fail "Langfuse failed after $MAX_RETRIES attempts"; $SVC_Langfuse = "Failed" }
        }
    }
}

# ===================================================================
# Summary
# ===================================================================
Write-Host ""
Write-Host "  =========================================================" -ForegroundColor Cyan
Write-Host "       SETUP SUMMARY                                       " -ForegroundColor Cyan
Write-Host "  =========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  CLI TOOLS:"
Write-Host "    Claude Code       : $Tool_Claude"
Write-Host "    Antigravity CLI   : $Tool_Antigravity"
Write-Host "    Bun               : $Tool_Bun"
Write-Host ""
Write-Host "  GIT:"
$gitUser  = git config --global user.name 2>$null
$gitEmail = git config --global user.email 2>$null
Write-Host "    User              : $gitUser <$gitEmail>"
Write-Host ""
Write-Host "  INFRASTRUCTURE:"
if ($wslOk) { Write-Host "    WSL               : Installed" } else { Write-Host "    WSL               : Not installed" }
Write-Host ""
Write-Host "  CONTAINERS:"
Write-Host "    Supabase          : $SVC_Supabase   http://localhost:3000"
Write-Host "    Langfuse          : $SVC_Langfuse   http://localhost:3001"
Write-Host ""
if ($API_KEY) {
    Write-Host "  API:"
    Write-Host "    Key               : $($API_KEY.Substring(0,8))..."
    Write-Host "    Base URL          : $BASE_URL"
} else {
    Write-Host "  API:                 Not configured"
}
Write-Host ""
Write-Host "  MCP SERVERS:           7 configured"
Write-Host "  SETTINGS FILE:         $SettingsFile"
Write-Host ""

if ($SVC_Supabase -eq "Running") {
    Write-Host "  -----------------------------------------------------------"
    Write-Host "  SERVICE URLS:"
    Write-Host "    Supabase Studio   : http://localhost:3000"
    Write-Host "    Supabase REST     : http://localhost:3100"
    Write-Host "    Supabase DB       : postgresql://supabase:$PG_PASSWORD@localhost:5432/supabase"
    Write-Host "    Langfuse          : http://localhost:3001"
    Write-Host "  -----------------------------------------------------------"
    Write-Host ""
}

if ($ErrorCount -gt 0) {
    Write-Host "  [WARN] $ErrorCount error(s) occurred during setup." -ForegroundColor Yellow
} else {
    Write-Ok "All steps completed successfully!"
}

Write-Host ""
Write-Host "  =========================================================" -ForegroundColor Cyan
Write-Host "  Happy hacking!" -ForegroundColor Cyan
Write-Host "  =========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  -----------------------------------------------------------" -ForegroundColor Yellow
Write-Host "  NOTES / POST-SETUP TO-DO:" -ForegroundColor Yellow
Write-Host "  -----------------------------------------------------------" -ForegroundColor Yellow
Write-Host "  1. Update your PATH to include: C:\Users\<YourUsername>\.local\bin" -ForegroundColor Yellow
Write-Host "     (This is needed for tools like Bun and other local binaries)" -ForegroundColor Yellow
Write-Host "     Run:  [Environment]::SetEnvironmentVariable('Path', `$env:Path + ';' + `$env:USERPROFILE + '\.local\bin', 'User')" -ForegroundColor Yellow
Write-Host "  2. Restart your terminal/PowerShell for PATH changes to take effect." -ForegroundColor Yellow
Write-Host "  -----------------------------------------------------------" -ForegroundColor Yellow
Write-Host ""
Read-Host "  Press Enter to exit"
