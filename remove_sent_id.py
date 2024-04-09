import os
import sys
def remove_sent_id(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the current item is a file
        if os.path.isfile(file_path):
            # Open the file for reading and writing
            with open(file_path, 'r+') as file:
                # Read the lines of the file
                lines = file.readlines()
                
                # Go back to the beginning of the file
                file.seek(0)
                
                # Rewrite the file without lines containing "sent_id"
                for line in lines:
                    if "sent_id" not in line:
                        file.write(line)
                
                # Truncate the remaining content if the new content is shorter
                file.truncate()

folder_path = sys.argv[1]
remove_sent_id(folder_path)
