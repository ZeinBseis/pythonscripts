import os
import stat

file_names = ['file1', 'file2', 'file3', 'file4']

#owner = read, right and execute.
#Group = read and right.
#Others = read only.

for file_name in file_names:
    # Check if the file exists
    if os.path.exists(file_name):
        # Set new file permissions
        os.chmod(file_name, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR |
                            stat.S_IRGRP | stat.S_IWGRP |
                            stat.S_IROTH)
        print(f"Changed file permissions for {file_name}")
    else:
        # Create the file if it doesn't exist
        with open(file_name, 'w') as file:
            file.write('This is a new file.')
        os.chmod(file_name, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR |
                            stat.S_IRGRP | stat.S_IWGRP |
                            stat.S_IROTH)
        print(f"Created file and set permissions: {file_name}")
