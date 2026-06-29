#!/usr/bin/env python3
"""
shutdown.py – Shut down the computer after a countdown.
Supports Windows, macOS and Linux.
"""

import sys
import time
import subprocess
import argparse

def shutdown_system():
    """Execute the appropriate shutdown command for the current OS."""
    if sys.platform == "win32":
        # Windows: /s = shutdown, /t 0 = immediately, /f = force close apps
        subprocess.run(["shutdown", "/s", "/t", "0", "/f"], check=True)
    elif sys.platform == "darwin":
        # macOS: -h = halt (shut down), now = immediately
        subprocess.run(["sudo", "shutdown", "-h", "now"], check=True)
    elif sys.platform.startswith("linux"):
        # Linux: systemctl poweroff works on most modern distros (no sudo needed
        # if the user is logged in locally with polkit permissions).
        # Fallback to shutdown -h now (may require sudo).
        try:
            subprocess.run(["systemctl", "poweroff", "-i"], check=True)
        except FileNotFoundError:
            subprocess.run(["sudo", "shutdown", "-h", "now"], check=True)
    else:
        print(f"Unsupported platform: {sys.platform}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Shut down the computer after a countdown.")
    parser.add_argument(
        "-t", "--time", type=int, default=10,
        help="Countdown time in seconds (default: 10)"
    )
    parser.add_argument(
        "-f", "--force", action="store_true",
        help="Skip the countdown and shut down immediately"
    )
    args = parser.parse_args()

    if args.force:
        print("Shutting down NOW!")
        shutdown_system()
    else:
        print(f"⚠️  System will shut down in {args.time} seconds.")
        print("   Press Ctrl+C to cancel.\n")
        try:
            for remaining in range(args.time, 0, -1):
                print(f"   {remaining:2d}...", end="\r")
                time.sleep(1)
            print("\nShutting down...")
            shutdown_system()
        except KeyboardInterrupt:
            print("\n\nShutdown aborted.")
            sys.exit(0)

if __name__ == "__main__":
    main()