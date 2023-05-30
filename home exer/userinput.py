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

# Prompt the user to input a date
target_date = input('Enter the date (YYYY-MM-DD): ')

# Filter the "upgrade" activities for the specified date
upgrade_logs = [log for log in logs_by_activity['upgrade'] if log.startswith(target_date)]

# Print the upgrade logs for the specified date
print('Upgrade activities on', target_date)
print('------------------------')
for log in upgrade_logs:
    print(log)
