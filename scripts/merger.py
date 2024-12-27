
import sys
import os
import natsort

# Take input folder name and output file name from command line arguments
input_folder_name = sys.argv[1]
output_file_name = sys.argv[2]

# List all files in the input folder and sort them naturally
folder_input = os.listdir(input_folder_name)
folder_input = natsort.natsorted(folder_input)  # Natural sort

# Open the output file in append mode with UTF-8 encoding
with open(output_file_name, 'a', encoding="utf-8") as wf:
    for filename in folder_input:
        # wf.write(filename + "\n")  # Write the filename
        wf.write("\n\n")
        with open(os.path.join(input_folder_name, filename), 'r', encoding="utf-8") as file:
            read = file.read()  # Read the content of the file
        wf.write(read + "\n" * 4)  # Write the content and insert four newlines after each file's content

print("--------------------")
print("Files have been merged.")
