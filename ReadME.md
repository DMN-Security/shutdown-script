# Shutdown Script

A simple, cross‑platform Python script to shut down your computer after a customizable countdown.  
Supports **Windows**, **macOS** and **Linux**.

## Features

- Automatic OS detection (Windows, macOS, Linux)
- Customisable countdown (default 10 seconds)
- Optional immediate shutdown with `--force`
- Graceful cancellation with `Ctrl+C`
- Easy to schedule via Task Scheduler (Windows) or cron (Linux/macOS)

## Requirements

- Python **3.6+** (standard library only, no external packages)
- Appropriate privileges:
  - **Windows**: no special rights needed
  - **macOS**: may require password for `sudo` unless configured otherwise
  - **Linux**: works without `sudo` on most modern desktop distributions (uses `systemctl poweroff -i`). For older systems or servers, `sudo` may be required.

## Installation

Clone the repository or simply download `shutdown.py`:

"bash"
git clone https://github.com/yourusername/shutdown-script.git
cd shutdown-script

## Usage
Run the script from a terminal:
python shutdown.py

## Command‑line options
Option	Description
-t, --time SECONDS	Set countdown length (default: 10)
-f, --force	Skip the countdown and shut down immediately
-h, --help	Show help message
Examples:

python shutdown.py --force          # immediate shutdown
python shutdown.py -t 5             # 5‑second countdown
python shutdown.py --time 60        # 1‑minute countdown

## Automation
Windows (Task Scheduler)
Open Task Scheduler and create a new task.

Set the trigger (time, event, etc.).

For Action, choose Start a program:

Program: pythonw.exe (to run without a console window)

Arguments: shutdown.py --force (use the full path)

Start in: the folder containing the script

## Linux / macOS (cron)
Add a cron job that runs the script with --force (example: shutdown every day at 23:00):

0 23 * * * /usr/bin/python3 /path/to/shutdown.py --force

On macOS, you may need to give cron full disk access (System Preferences → Security & Privacy → Privacy → Full Disk Access).
If the script requires sudo, either run it with sudo and configure passwordless sudo for the shutdown command, or use systemctl poweroff (which often works without sudo on desktop Linux).

## Important notes
On Windows, the command shutdown /s /f is used – open applications will be force closed without asking to save.

On macOS, sudo shutdown -h now will prompt for your password unless you have edited /etc/sudoers.

On Linux, the script attempts systemctl poweroff -i first. If systemctl is not found, it falls back to sudo shutdown -h now.

Always test the script when you can afford an unexpected shutdown. The --force flag shuts down immediately – use with care.

## License
This project is licensed under the MIT License. You’re free to use, modify and distribute it.

Happy automating! ⚡