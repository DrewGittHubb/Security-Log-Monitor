# Security Log Monitor

A real-time log monitoring and alerting tool built in Python for Security Automation class (June 2026).

## What It Does
Continuously watches a log file for security events and sends instant alerts to Discord when threats are detected, including:
- Failed login attempts
- Brute-force attacks
- Unauthorized access attempts
- Invalid user attempts
- Sudo escalation attempts
- Critical system events

## How to Run
1. Clone this repository
2. Add your Discord webhook URL to line 33 of `log_monitor.py`
3. Run the script:
python log_monitor.py
4. In a second terminal, append suspicious log lines to `server_access.log` to trigger alerts

## Webhook Setup
1. Go to your Discord server → Edit Channel → Integrations → Webhooks → New Webhook
2. Copy the webhook URL
3. Open `log_monitor.py` and replace the placeholder on line 33:
   `WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL_HERE"`
4. Save the file before running the script

## Testing
python log_monitor.py --file server_access.log

## Prerequisites
Python 3.x is required. No additional installations or pip packages needed — the script runs entirely on the Python standard library.

## Dependencies
None — built entirely with Python standard library. No pip installs required.

## What Triggers an Alert
The following patterns in your log file will trigger an immediate Discord alert:
- `Failed password` / `login failed` → FAILED_LOGIN
- `Failed password for ... from ... port` → BRUTE_FORCE
- `Unauthorized` / `permission denied` → UNAUTHORIZED_ACCESS
- `Invalid user` / `unknown user` → INVALID_USER
- `sudo: ... COMMAND` → SUDO_ATTEMPT
- `CRITICAL` / `EMERGENCY` / `ALERT` → CRITICAL_EVENT

## Security Note
The Discord webhook URL is intentionally left as a placeholder. Never commit real API keys or webhook URLs to GitHub.

## Author
Andrew Avila — Security Automation Class — June 2026
