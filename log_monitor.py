#!/usr/bin/env python3
"""
Project #5: Log Monitoring and Alerting System
Security Automation Class - June 2026

A real-time log monitoring tool (tail -f style) that detects security events
and sends rich alerts to Discord.
"""

import time
import os
import json
import urllib.request
import argparse
import re
from datetime import datetime
from typing import Dict

# ========================= CONFIGURATION =========================
DEFAULT_LOG_PATH = "server_access.log"

# Modern security detection patterns
SECURITY_PATTERNS: Dict[str, str] = {
    "failed_login": r"Failed password|authentication failure|login failed",
    "brute_force": r"Failed password for .* from .* port",
    "unauthorized_access": r"Unauthorized|permission denied|access denied",
    "invalid_user": r"Invalid user|unknown user",
    "sudo_attempt": r"sudo: .* COMMAND|attempt to use sudo",
    "critical_event": r"CRITICAL|EMERGENCY|ALERT"
}

# ←←← CHANGE THIS TO YOUR DISCORD WEBHOOK URL ←←←
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL_HERE"

# Alert counter
alert_count: int = 0


def send_discord_alert(event_type: str, log_line: str) -> bool:
    """Send rich formatted alert to Discord."""
    global alert_count
    alert_count += 1

    payload = {
        "username": "Security Monitor",
        "embeds": [{
            "title": "🚨 SECURITY ALERT",
            "color": 0xFF0000,
            "timestamp": datetime.now().isoformat(),
            "fields": [
                {"name": "Event Type", "value": event_type.upper(), "inline": True},
                {"name": "Alert #", "value": str(alert_count), "inline": True},
                {"name": "Log Entry", "value": f"```\n{log_line[:500]}\n```"}
            ],
            "footer": {"text": "Security Automation Project #5"}
        }]
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            WEBHOOK_URL,
            data=data,
            headers={
                'User-Agent': 'Mozilla/5.0',
                'Content-Type': 'application/json'
            },
            method='POST'
        )

        with urllib.request.urlopen(req) as response:
            if response.status in (200, 204):
                print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Alert #{alert_count} sent to Discord")
                return True
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Failed to send alert: {e}")
        return False
    return False


def monitor_log(target_file: str):
    """Main real-time monitoring function."""
    print(f"[{datetime.now()}] 🚀 Security Log Monitor v2026 Started")
    print(f"Watching → {target_file}")
    print("Press Ctrl+C to stop monitoring\n")

    if not os.path.exists(target_file):
        print(f"❌ Error: {target_file} not found!")
        print("Please create the log file first.")
        return

    with open(target_file, "r", encoding="utf-8") as file:
        file.seek(0, os.SEEK_END)        # Jump to end of file (tail -f style)

        while True:
            line = file.readline()

            if line:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                # Pattern matching
                for event_name, pattern in SECURITY_PATTERNS.items():
                    if re.search(pattern, cleaned_line, re.IGNORECASE):
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚠️  {event_name.upper()} DETECTED!")
                        print(f"   {cleaned_line[:150]}...\n")

                        send_discord_alert(event_name, cleaned_line)
                        break
            else:
                time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-time Security Log Monitor")
    parser.add_argument("--file", default=DEFAULT_LOG_PATH, help="Path to log file to monitor")
    args = parser.parse_args()

    try:
        monitor_log(args.file)
    except KeyboardInterrupt:
        print(f"\n[{datetime.now()}] 👋 Monitoring stopped. Total alerts: {alert_count}")
    except Exception as e:
        print(f"Unexpected error: {e}")