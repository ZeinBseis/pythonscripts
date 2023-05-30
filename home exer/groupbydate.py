import re

logs = '''Jun  1 22:20:05 secserv kernel: Kernel logging (proc) stopped.
Jun  1 22:20:05 secserv kernel: Kernel log daemon terminating.
Jun  1 22:20:06 secserv exiting on signal 15
Nov 27 08:05:57 galileo kernel: Kernel logging (proc) stopped.
Nov 27 08:05:57 galileo kernel: Kernel log daemon terminating.
Nov 27 08:05:57 galileo exiting on signal 15'''

log_lines = logs.splitlines()
logs_by_date = {}

# Group logs by date
for line in log_lines:
    match = re.search(r'^\w{3}\s+\d{1,2}', line)
    if match:
        date = match.group()
        if date not in logs_by_date:
            logs_by_date[date] = []
        logs_by_date[date].append(line)

# Print logs grouped by date
for date, logs in logs_by_date.items():
    print(f"Logs for date: {date}")
    for log in logs:
        print(log)
    print()
