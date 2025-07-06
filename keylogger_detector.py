import psutil

suspicious_keywords = ["keylogger", "pynput", "keyboard", "log_keys", "hook", "record_keys"]

print(" Scanning for suspicious processes...\n")

for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        process_name = proc.info['name']
        cmdline_list = proc.info['cmdline']

        if cmdline_list and isinstance(cmdline_list, list):
            process_cmdline = ' '.join(cmdline_list)

            for keyword in suspicious_keywords:
                if keyword.lower() in process_cmdline.lower():
                    print(f" Suspicious process found!")
                    print(f"PID: {proc.info['pid']}")
                    print(f"Name: {process_name}")
                    print(f"Command: {process_cmdline}\n")
                    break

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

print("Scan complete.")
