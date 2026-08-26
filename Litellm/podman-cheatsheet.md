# 🐳 Podman Cheatsheet

## 📥 Installation

```powershell
# Install Podman CLI on Windows
winget install RedHat.Podman

# Initialize Podman machine (first time)
podman machine init

# Set rootful mode (better port forwarding)
podman machine set --rootful

# Start the machine
podman machine start
```

---

## 🖥️ Machine Management

| Emoji | Command | Description |
|-------|---------|-------------|
| 🚀 | `podman machine start` | Start the Podman VM |
| 🛑 | `podman machine stop` | Stop the Podman VM |
| 📋 | `podman machine list` | List all machines |
| 🔌 | `podman machine ssh` | SSH into the VM (Linux only) |
| 🗑️ | `podman machine rm <name>` | Delete a machine |
| ℹ️ | `podman machine info` | Show machine details |
| 🔧 | `podman machine set --rootful` | Enable rootful mode |

---

## 📦 Image Commands

| Emoji | Command | Description |
|-------|---------|-------------|
| ⬇️ | `podman pull <image>` | Pull an image |
| 🔓 | `podman pull --tls-verify=false <image>` | Pull skipping TLS (corp proxy fix) |
| 📋 | `podman images` | List all images |
| 🗑️ | `podman rmi <image>` | Remove an image |
| 🧹 | `podman image prune -a` | Remove all unused images |
| 🔍 | `podman search <term>` | Search for images |
| 🏗️ | `podman build -t <name> .` | Build image from Dockerfile |
| 💾 | `podman save -o file.tar <image>` | Export image to tar |
| 📂 | `podman load -i file.tar` | Import image from tar |

---

## 🏃 Container Commands

| Emoji | Command | Description |
|-------|---------|-------------|
| ▶️ | `podman run -d -p 8080:80 <image>` | Run container (detached + port) |
| 📋 | `podman ps` | List running containers |
| 📋 | `podman ps -a` | List ALL containers (incl. stopped) |
| 🛑 | `podman stop <name>` | Stop a container |
| ▶️ | `podman start <name>` | Start a stopped container |
| 🔄 | `podman restart <name>` | Restart a container |
| 🗑️ | `podman rm <name>` | Remove a container |
| 🗑️ | `podman rm -f <name>` | Force remove (even if running) |
| 💀 | `podman kill <name>` | Kill a container immediately |

---

## 🔍 Inspect & Debug

| Emoji | Command | Description |
|-------|---------|-------------|
| 📝 | `podman logs <name>` | View container logs |
| 📝 | `podman logs -f <name>` | Follow logs (live) |
| 📝 | `podman logs --tail 50 <name>` | Last 50 lines of logs |
| 🔎 | `podman inspect <name>` | Full container details (JSON) |
| 🖥️ | `podman exec -it <name> bash` | Shell into a running container |
| 🖥️ | `podman exec -it <name> sh` | Shell (Alpine/minimal images) |
| 📊 | `podman stats` | Live resource usage (CPU/RAM) |
| 🔌 | `podman port <name>` | Show port mappings |
| 🏥 | `podman healthcheck run <name>` | Run healthcheck manually |
| 📂 | `podman cp <name>:/path ./local` | Copy file from container |

---

## 🎼 Compose Commands

| Emoji | Command | Description |
|-------|---------|-------------|
| 🚀 | `podman compose up -d` | Start all services (detached) |
| 🛑 | `podman compose down` | Stop and remove all services |
| 🛑 | `podman compose down -v` | Stop + remove volumes too |
| 📋 | `podman compose ps` | List compose services |
| 📝 | `podman compose logs` | View all service logs |
| 📝 | `podman compose logs -f <svc>` | Follow one service's logs |
| 🔄 | `podman compose restart <svc>` | Restart one service |
| 🏗️ | `podman compose build` | Build/rebuild images |
| ⬇️ | `podman compose pull` | Pull latest images |

---

## 🌐 Network Commands

| Emoji | Command | Description |
|-------|---------|-------------|
| 📋 | `podman network ls` | List networks |
| ➕ | `podman network create <name>` | Create a network |
| 🗑️ | `podman network rm <name>` | Remove a network |
| 🔎 | `podman network inspect <name>` | Inspect network details |

---

## 💾 Volume Commands

| Emoji | Command | Description |
|-------|---------|-------------|
| 📋 | `podman volume ls` | List volumes |
| ➕ | `podman volume create <name>` | Create a volume |
| 🗑️ | `podman volume rm <name>` | Remove a volume |
| 🧹 | `podman volume prune` | Remove unused volumes |
| 🔎 | `podman volume inspect <name>` | Inspect volume details |

---

## 🧹 Cleanup Commands

| Emoji | Command | Description |
|-------|---------|-------------|
| 🧹 | `podman system prune` | Remove unused data |
| 💣 | `podman system prune -a --volumes` | Remove EVERYTHING unused |
| 📊 | `podman system df` | Show disk usage |
| ℹ️ | `podman info` | Full system info |
| 🔄 | `podman system reset` | Factory reset (nuclear option) |

---

## 🏢 Corporate Proxy / TLS Fixes

```powershell
# Pull images bypassing TLS verification (corp proxy)
podman pull --tls-verify=false ghcr.io/berriai/litellm:main-latest

# Check WSL VM IP (when localhost doesn't work)
wsl -d podman-machine-default -- ip addr show eth0

# Test connectivity inside WSL
wsl -d podman-machine-default -- curl -s http://localhost:4000/health

# Port forward WSL → Windows (run as Admin)
netsh interface portproxy add v4tov4 listenport=4000 listenaddress=127.0.0.1 connectport=4000 connectaddress=<WSL_IP>

# View active port forwards
netsh interface portproxy show v4tov4

# Remove a port forward
netsh interface portproxy delete v4tov4 listenport=4000 listenaddress=127.0.0.1
```

---

## ⚡ Quick Reference

```powershell
# Full startup sequence (corporate machine)
podman machine start
podman pull --tls-verify=false <image>
podman compose up -d
podman ps
podman logs <container>

# Full shutdown
podman compose down
podman machine stop

# Reinstall from scratch
podman compose down -v
podman machine stop
podman machine rm podman-machine-default
podman machine init
podman machine set --rootful
podman machine start
```
