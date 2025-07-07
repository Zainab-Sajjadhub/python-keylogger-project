## Python-keylogger-project
# Educational Keylogger & Detector

This repository contains two simple Python scripts for educational purposes:

- `keylogger.py`: A basic keylogger that records keystrokes to a local file.
- `keylogger_detector.py`: A process scanner that searches running processes for suspicious keywords related to keyloggers.

---

## ⚠️ Disclaimer

This project is strictly for **educational and ethical use only**.  
Do **NOT** use these scripts to monitor or capture input from anyone without explicit permission.  

---

## Features

- Demonstrates how keylogging works using the `pynput` library.
- Detects potentially malicious processes by scanning running processes with `psutil`.
- Logs findings to files (`key_log.txt` and `suspicious_activity.log`).
