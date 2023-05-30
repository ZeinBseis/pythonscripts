import re

log_file_path = 'alternatives.log'

# Regular expression pattern to extract date from log entries
date_pattern = r'(\d{4}-\d{2}-\d{2})'

# Dictionary to store logs grouped by date
logs_by_date = {}

# Open the log file and read its contents
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        # Extract the date from the log entry
        match = re.search(date_pattern, line)
        if match:
            date = match.group(1)
            # Add the log entry to the corresponding date group
            if date in logs_by_date:
                logs_by_date[date].append(line)
            else:
                logs_by_date[date] = [line]

# Print the logs grouped by date
for date, logs in logs_by_date.items():
    print('Logs for date:', date)
    print('------------------------')
    for log in logs:
        print(log)
    print()
