# 🧹 Chris's VM Universal Cleanup Utility

### 🔍 Overview
A specialized Python automation script developed to resolve the **"No space left on device" (StorageFull)** error frequently encountered in Ubuntu-based cybersecurity lab environments. 

In virtualized environments running Docker and VS Code Server, disk space is often consumed by orphaned image layers and system logs, preventing new lab provisioning. This tool automates the reclamation of several gigabytes of storage in seconds.

### 🛠️ Automation Sequence
The script executes a multi-stage cleanup flow:
1. **System Audit:** Checks current disk usage via `df -h`.
2. **Docker Purge:** Forcefully prunes all unused containers, networks, and dangling image layers.
3. **Log Rotation:** Vacuums system journals to the last 1 second of data.
4. **Package Management:** Cleans the APT cache and removes unneeded dependencies.
5. **Cache Reset:** Clears user-level caches to ensure a clean state for VS Code extensions.

### 💻 Usage
Designed for instant deployment via terminal:
```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/chris12x1/cybersecurity-projects/main/secops-automation/vm-infrastructure-utils/chrisVMcleanup.py)"
