import os
import stat

file_path = '/path/to/file1'

#owner = read, right and execute
#Group = read and right only
#Others = read only 

#stat.S_IRUSR for owner read permission, stat.S_IWUSR for owner write permission, 
#stat.S_IXUSR for owner execute permission,

# Check if the file exists
if os.path.exists(file_path):
    # Set new file permissions
    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR |
                     stat.S_IRGRP | stat.S_IWGRP |
                     stat.S_IROTH)

    print(f"Changed file permissions for {file_path}")
else:
    print(f"File does not exist: {file_path}")
