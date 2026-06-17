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

## Testing
python log_monitor.py --file server_access.log

## Dependencies
None — built entirely with Python standard library. No pip installs required.

## Security Note
The Discord webhook URL is intentionally left as a placeholder. Never commit real API keys or webhook URLs to GitHub.

## Author
Security Automation Class — June 2026
