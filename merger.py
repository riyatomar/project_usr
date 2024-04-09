import sys
import os

input_folder_name = sys.argv[1]
output_file_name = sys.argv[2]
folder_input = os.listdir(input_folder_name)
folder_input.sort()

with open(output_file_name, 'a', encoding="utf-8") as wf:
    for filename in folder_input:
        wf.write(filename + "\n")
        with open(os.path.join(input_folder_name, filename), 'r', encoding="utf-8") as file:
            read = file.read()

        wf.write(read + "\n" * 4)  # Insert four newlines after each file's content
        
print("--------------------")
print("Files have been merged.")