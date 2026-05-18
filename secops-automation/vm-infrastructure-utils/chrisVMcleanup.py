import subprocess
import os
import sys

def run_cmd(cmd):
    try:
        # Runs the shell command and returns the output
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
        return result
    except subprocess.CalledProcessError as e:
        return f"Note: {cmd} skipped or returned an error."

def main():
    print("\n" + "!" * 50)
    print("⚠️  WARNING: TOTAL SYSTEM CLEANUP INITIATED")
    print("!" * 50)
    print("This script will SHUT DOWN all running Docker containers and")
    print("PERMANENTLY DELETE all unused images, networks, and caches.")
    print("Ensure you have saved all work before proceeding.")
    print("!" * 50 + "\n")

    confirm = input("Do you want to continue? (y/n): ").lower()
    if confirm != 'y':
        print("\n❌ Cleanup aborted by user. No changes made.")
        sys.exit()

    print("\n🚀 Starting Chris's VM Universal Cleanup...")
    print("=" * 50)

    # Stage 1: Initial Space Check
    print("📊 INITIAL DISK USAGE:")
    print(run_cmd("df -h / | grep /"))

    # Stage 2: Execution of Universal Cleanup Commands
    commands = [
        "sudo apt-get clean",
        "sudo apt-get autoremove -y",
        "sudo docker stop $(sudo docker ps -q)",
        "sudo docker compose down",
        "sudo docker system prune -a -f",
        "sudo docker image prune -a -f",
        "sudo journalctl --vacuum-time=1s",
        "rm -rf ~/.cache/*"
    ]

    print("\n🧹 Executing cleanup sequence...")
    for cmd in commands:
        print(f"-> Running: {cmd}...")
        run_cmd(cmd)

    print("=" * 50)

    # Stage 3: Final Space Check
    print("✅ CLEANUP COMPLETE. RECLAIMED SPACE RESULTS:")
    print(run_cmd("df -h / | grep /"))
    print("\nEnvironment ready. Re-run your provision script to start a fresh lab!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped by user (Ctrl+C). Exiting...")
