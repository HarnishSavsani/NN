# ╔══════════════════════════════════════════════════════════════╗
# ║  🚀 LiteLLM + Langfuse — One-Click Setup Script            ║
# ║  Sets up Podman, pulls images, generates configs, starts    ║
# ║  everything. Just run and follow the prompts!               ║
# ╚══════════════════════════════════════════════════════════════╝

param(
    [string]$ApiKey,
    [string]$BaseUrl,
    [string]$Password = "nexus!123",
    [switch]$SkipPodmanInit,
    [switch]$SkipPull
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# ── Helper Functions ──────────────────────────────────────────

function Write-Step($emoji, $msg) {
    Write-Host ""
    Write-Host "  $emoji  $msg" -ForegroundColor Cyan
    Write-Host "  $('─' * 60)" -ForegroundColor DarkGray
}

function Write-Ok($msg) {
    Write-Host "  ✅  $msg" -ForegroundColor Green
}

function Write-Warn($msg) {
    Write-Host "  ⚠️  $msg" -ForegroundColor Yellow
}

function Write-Fail($msg) {
    Write-Host "  ❌  $msg" -ForegroundColor Red
}

# ── Banner ────────────────────────────────────────────────────

Write-Host ""
Write-Host "  ╔══════════════════════════════════════════════════╗" -ForegroundColor Magenta
Write-Host "  ║   🐳 LiteLLM + Langfuse Setup Wizard            ║" -ForegroundColor Magenta
Write-Host "  ║   Corporate-friendly • TLS-skip • Auto-config    ║" -ForegroundColor Magenta
Write-Host "  ╚══════════════════════════════════════════════════╝" -ForegroundColor Magenta
Write-Host ""

# ── Step 1: Collect Inputs ────────────────────────────────────

Write-Step "🔑" "Configuration"

if (-not $BaseUrl) {
    $BaseUrl = Read-Host "  Enter your LLM API Base URL (e.g. https://genailab.tcs.in)"
}
$BaseUrl = $BaseUrl.TrimEnd('/')

if (-not $ApiKey) {
    $ApiKey = Read-Host "  Enter your API Key"
}

$MasterKey = "sk-nexus!123"
$UiUser = "admin"
$UiPass = $Password
$SaltKey = "4e657572616c4e6578757353616c7432303236303030303030303030303030303030"
$EncryptionKey = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
$DbPass = $Password
$DbPassEncoded = $DbPass -replace '!', '%21'

Write-Ok "Base URL  : $BaseUrl"
Write-Ok "API Key   : $($ApiKey.Substring(0,6))***"
Write-Ok "UI Login  : $UiUser / $UiPass"
Write-Ok "Master Key: $MasterKey"

# ── Step 2: Podman Machine Setup ──────────────────────────────

if (-not $SkipPodmanInit) {
    Write-Step "🖥️" "Setting up Podman Machine"

    # Check if Podman is installed
    try {
        $podmanVer = podman --version
        Write-Ok "Podman found: $podmanVer"
    } catch {
        Write-Fail "Podman not installed! Install from: https://github.com/containers/podman/releases/latest"
        Write-Host "  Then re-run this script." -ForegroundColor Yellow
        exit 1
    }

    # Check if machine exists
    $machineList = podman machine list --format "{{.Name}}" 2>$null
    if ($machineList -match "podman-machine-default") {
        Write-Warn "Podman machine already exists — skipping init"
    } else {
        Write-Host "  Initializing Podman machine..." -ForegroundColor Gray
        podman machine init
        Write-Ok "Machine initialized"
    }

    # Set rootful
    Write-Host "  Setting rootful mode..." -ForegroundColor Gray
    podman machine set --rootful 2>$null
    Write-Ok "Rootful mode set"

    # Start machine
    $machineInfo = podman machine list --format "{{.LastUp}}" 2>$null
    if ($machineInfo -match "Currently running") {
        Write-Warn "Machine already running"
    } else {
        Write-Host "  Starting Podman machine..." -ForegroundColor Gray
        podman machine start
        Write-Ok "Machine started"
    }
} else {
    Write-Step "⏭️" "Skipping Podman machine setup (--SkipPodmanInit)"
}

# ── Step 3: Pull Images ──────────────────────────────────────

if (-not $SkipPull) {
    Write-Step "📥" "Pulling container images (TLS verify disabled for corp proxy)"

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
        Write-Host "  ⬇️  Pulling $shortName ..." -ForegroundColor Gray -NoNewline
        podman pull --tls-verify=false $img 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host " ✅" -ForegroundColor Green
        } else {
            Write-Host " ❌ (may already exist locally)" -ForegroundColor Yellow
        }
    }
    Write-Ok "All images pulled"
} else {
    Write-Step "⏭️" "Skipping image pull (--SkipPull)"
}

# ── Step 4: Generate init-db.sql ──────────────────────────────

Write-Step "🗄️" "Generating init-db.sql"

$initDbContent = "CREATE DATABASE litellm;"
Set-Content -Path "$ScriptDir\init-db.sql" -Value $initDbContent -Encoding utf8
Write-Ok "init-db.sql created"

# ── Step 5: Fetch models & generate litellm_config.yaml ───────

Write-Step "🤖" "Fetching available models from $BaseUrl"

try {
    $modelsJson = wsl -d podman-machine-default -- curl -sk "$BaseUrl/v1/models" -H "Authorization: Bearer $ApiKey" 2>$null
    $models = ($modelsJson | ConvertFrom-Json).data
    Write-Ok "Found $($models.Count) models"
} catch {
    Write-Fail "Could not fetch models. Check your Base URL and API Key."
    Write-Host "  Error: $_" -ForegroundColor Red
    exit 1
}

# Build YAML
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
      api_base: $BaseUrl/v1
      api_key: $ApiKey
"@

    # Add model_info if token limits are available
    $hasInput = $null -ne $m.max_input_tokens -and $m.max_input_tokens -gt 0
    $hasOutput = $null -ne $m.max_output_tokens -and $m.max_output_tokens -gt 0
    if ($hasInput -or $hasOutput) {
        $yaml += "`n      model_info:"
        if ($hasInput) {
            $yaml += "`n        max_input_tokens: $($m.max_input_tokens)"
        }
        if ($hasOutput) {
            $yaml += "`n        max_output_tokens: $($m.max_output_tokens)"
        }
    }
}

Set-Content -Path "$ScriptDir\litellm_config.yaml" -Value $yaml -Encoding utf8
Write-Ok "litellm_config.yaml created with $($models.Count) models"

# ── Step 6: Generate docker-compose.yml ───────────────────────

Write-Step "📝" "Generating docker-compose.yml"

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

# ── Step 7: Port Forwarding Setup ─────────────────────────────

Write-Step "🌐" "Setting up port forwarding (WSL → Windows)"

# Get WSL IP
try {
    $wslIpRaw = wsl -d podman-machine-default -- ip -4 addr show eth0 2>$null
    $wslIp = ($wslIpRaw | Select-String -Pattern 'inet (\d+\.\d+\.\d+\.\d+)').Matches.Groups[1].Value

    if ($wslIp) {
        Write-Ok "WSL IP: $wslIp"
        Write-Host ""
        Write-Host "  ⚠️  Port forwarding requires Admin PowerShell." -ForegroundColor Yellow
        Write-Host "  Run this in an elevated (Admin) PowerShell:" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "  netsh interface portproxy add v4tov4 listenport=4000 listenaddress=127.0.0.1 connectport=4000 connectaddress=$wslIp" -ForegroundColor White
        Write-Host "  netsh interface portproxy add v4tov4 listenport=3000 listenaddress=127.0.0.1 connectport=3000 connectaddress=$wslIp" -ForegroundColor White
        Write-Host ""

        # Save to a helper script
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
    Write-Warn "Could not detect WSL IP — set up port forwarding manually"
}

# ── Step 8: Start Services ────────────────────────────────────

Write-Step "🚀" "Starting all services"

podman compose up -d
if ($LASTEXITCODE -eq 0) {
    Write-Ok "All services started!"
} else {
    Write-Fail "Compose failed — check errors above"
    exit 1
}

# Wait for health
Write-Host "  ⏳  Waiting for services to become healthy..." -ForegroundColor Gray
Start-Sleep -Seconds 20

# ── Summary ───────────────────────────────────────────────────

Write-Host ""
Write-Host "  ╔══════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "  ║   🎉  Setup Complete!                            ║" -ForegroundColor Green
Write-Host "  ╠══════════════════════════════════════════════════╣" -ForegroundColor Green
Write-Host "  ║                                                  ║" -ForegroundColor Green
Write-Host "  ║   LiteLLM UI : http://localhost:4000/ui          ║" -ForegroundColor Green
Write-Host "  ║   Langfuse   : http://localhost:3000             ║" -ForegroundColor Green
Write-Host "  ║                                                  ║" -ForegroundColor Green
Write-Host "  ║   UI Login   : admin / $UiPass              ║" -ForegroundColor Green
Write-Host "  ║   Master Key : $MasterKey                ║" -ForegroundColor Green
Write-Host "  ║   Models     : $($models.Count) auto-discovered           ║" -ForegroundColor Green
Write-Host "  ║                                                  ║" -ForegroundColor Green
Write-Host "  ║   📌 If localhost doesn't work, run as Admin:    ║" -ForegroundColor Yellow
Write-Host "  ║      .\enable-ports.ps1                          ║" -ForegroundColor Yellow
Write-Host "  ║                                                  ║" -ForegroundColor Green
Write-Host "  ║   📌 Next: Sign into Langfuse, create API keys, ║" -ForegroundColor Green
Write-Host "  ║   then update LANGFUSE_SECRET/PUBLIC_KEY in      ║" -ForegroundColor Green
Write-Host "  ║   docker-compose.yml and restart litellm.        ║" -ForegroundColor Green
Write-Host "  ║                                                  ║" -ForegroundColor Green
Write-Host "  ╚══════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

# Show running containers
podman ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
