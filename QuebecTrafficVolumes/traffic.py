import os

def count_files(folder_path, subfolders, separator, suffix):
    # Initialize counters
    folder_count = 0
    file_count = 0

    # Iterate over subfolders
    for subfolder in subfolders:
        # Get the list of files in the subfolder
        files = os.listdir(os.path.join(folder_path, subfolder))

        # Check if the subfolder contains the specified files
        files_present = any(file.startswith(subfolder) and separator in file and suffix in file for file in files)

        # Increment counters
        if files_present:
            folder_count += 1
            file_count += sum(file.startswith(subfolder) and separator in file and suffix in file for file in files)

    return folder_count, file_count
