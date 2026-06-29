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

```bash
git clone https://github.com/DMN-Security/Shutdown-script.git
cd Shutdown-script