import re

# Read the contents of the file
with open("alternatives.log", "r") as file:
    log_data = file.read()

# Define the regex pattern for date extraction
date_pattern = r"(\d{4}-\d{2}-\d{2})"

# Find all unique dates in the log data
dates = sorted(set(re.findall(date_pattern, log_data)))

# Group logs by date
logs_by_date = {}
for date in dates:
    logs_by_date[date] = re.findall(date + r".*?(?=\n\d{4}-\d{2}-\d{2}|$)", log_data, re.DOTALL)

# Print logs grouped by date
for date, logs in logs_by_date.items():
    print(f"Logs for date {date}:")
    for log in logs:
        print(log)
    print()
