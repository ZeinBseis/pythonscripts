import os
import stat

files = ['/path/to/file1', '/path/to/file2', '/path/to/file3']

for file_path in files:
    # Check if the file exists
    if not os.path.exists(file_path):
        # Create the file if it doesn't exist
        open(file_path, 'w').close()
        print(f"Created file: {file_path}")

    # Check the file permissions
    mode = os.stat(file_path).st_mode
    owner_executable = bool(mode & stat.S_IXUSR)
    group_executable = bool(mode & stat.S_IXGRP)

    # Add execution permission for owner if missing
    if not owner_executable:
        mode |= stat.S_IXUSR
        os.chmod(file_path, mode)
        print(f"Added execution permission for owner: {file_path}")

    # Add execution permission for group if missing
    if not group_executable:
        mode |= stat.S_IXGRP
        os.chmod(file_path, mode)
        print(f"Added execution permission for group: {file_path}")
