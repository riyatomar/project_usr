import os
import sys

textfile = sys.argv[1]
output_folder = sys.argv[2]
os.makedirs(output_folder, exist_ok=True)

with open(textfile, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize variables to track the current filename and its content
current_filename = None
current_content = []

# Loop through the lines in the file
for line in lines:
    try:
        if current_filename is None and line.startswith("Geo_nios") and ":coref" not in line:
            current_filename = line.strip()
            current_content = []
        elif current_filename is not None:
            current_content.append(line)

            # Check if we have collected 11 lines of content
            if len(current_content) == 11:
                # Create a file with the current_filename and write the content to it
                with open(os.path.join(output_folder, current_filename + ".txt"), "w", encoding="utf-8") as output_file:
                    output_file.writelines(current_content)

                # Reset the current_filename and content variables
                current_filename = None
                current_content = []
    except Exception as e:
        # Handle the exception by printing an error message and continue to the next item
        print(f"Error processing item: {e}")

# Check if there's any remaining content that wasn't written to a file
if current_filename is not None and current_content:
    with open(os.path.join(output_folder, current_filename + ".txt"), "w", encoding="utf-8") as output_file:
        output_file.writelines(current_content)

print("Files have been saved to the output folder.")
