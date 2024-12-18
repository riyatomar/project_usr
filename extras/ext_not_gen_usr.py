# import os
# from pathlib import Path
# import sys

# def check_files_in_directory(directory):
#     # Convert the directory to a Path object for ease of use
#     path = Path(directory)
    
#     # Ensure the provided directory exists
#     if not path.is_dir():
#         print(f"The directory {directory} does not exist.")
#         return

#     # Get a sorted list of all files in the directory
#     files = sorted(path.iterdir())

#     # Iterate over all files in the sorted list
#     for file_path in files:
#         # Check if the current path is a file
#         if file_path.is_file():
#             # Read the file and count the number of lines
#             with open(file_path, 'r') as file:
#                 lines = file.readlines()
#                 # Check if the file does not contain 11 lines
#                 if len(lines) != 11:
#                     print(f"Deleting {file_path.name} (has {len(lines)} lines)")
#                     file_path.unlink()  # Delete the file

# # Example usage
# check_files_in_directory(sys.argv[1])


import os
from pathlib import Path
import sys

def check_files_in_directory(directory):
    # Convert the directory to a Path object for ease of use
    path = Path(directory)
    
    # Ensure the provided directory exists
    if not path.is_dir():
        print(f"The directory {directory} does not exist.")
        return

    # Get a sorted list of all files in the directory
    files = sorted(path.iterdir())

    # Iterate over all files in the sorted list
    for file_path in files:
        # Check if the current path is a file
        if file_path.is_file():
            # Read the file and count the number of lines
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # Check if the file does not contain 11 lines
                if len(lines) != 9 and len(lines) != 6:
                    print(f"{file_path.name}")# (has {len(lines)} lines)")
                    # file_path.unlink()  # Delete the file
# Example usage
check_files_in_directory(sys.argv[1])
