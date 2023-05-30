import re

log_file_path = 'dpkg.log'

# Dictionary to store logs grouped by activity
logs_by_activity = {'install': [], 'status': [], 'upgrade': []}

# Regex pattern to match the log entry format
log_entry_pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$'

# Open the log file and read its contents
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        # Extract the date, time, activity, and log message using regex
        match = re.match(log_entry_pattern, line.strip())
        if match:
            date_time = match.group(1)
            activity = match.group(2)
            log_message = match.group(3)
            
            # Append the log entry to the corresponding activity group
            if activity in logs_by_activity:
                logs_by_activity[activity].append(line.strip())

# Print the logs grouped by activity
for activity, logs in logs_by_activity.items():
    print('Logs for activity:', activity)
    print('------------------------')
    for log in logs:
        print(log)
    print()
