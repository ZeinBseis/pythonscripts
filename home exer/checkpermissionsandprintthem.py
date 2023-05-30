import os
import stat

file_path = '/path/to/file1'

# Check if the file exists
if os.path.exists(file_path):
    # Get the file permissions
    permissions = stat.filemode(os.stat(file_path).st_mode)
    print(f"File permissions for {file_path}: {permissions}")
else:
    print(f"File does not exist: {file_path}")
