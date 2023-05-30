import os
import stat

files = ['file1', 'file2', 'file3']

for file_name in files:
    # Check if the file exists
    if not os.path.exists(file_name):
        # Create the file if it doesn't exist
        with open(file_name, 'w'):
            pass
        print(f"Created file: {file_name}")

    # Check the file permissions
    mode = os.stat(file_name).st_mode
    owner_executable = bool(mode & stat.S_IXUSR)
    group_executable = bool(mode & stat.S_IXGRP)

    # Add execution permission for owner if missing
    if not owner_executable:
        mode |= stat.S_IXUSR
        os.chmod(file_name, mode)
        print(f"Added execution permission for owner: {file_name}")

    # Add execution permission for group if missing
    if not group_executable:
        mode |= stat.S_IXGRP
        os.chmod(file_name, mode)
        print(f"Added execution permission for group: {file_name}")

