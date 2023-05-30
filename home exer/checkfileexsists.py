import os

file_path = '/path/to/file1'

# Check if the file exists
if not os.path.exists(file_path):
    # Create the file if it doesn't exist
    with open(file_path, 'w') as file:
        file.write('This is a new file.')
    print(f"Created file: {file_path}")
else:
    print(f"File already exists: {file_path}")
