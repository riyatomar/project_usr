# import os

# def process_files(folder_path):
#     # Iterate over all files in the folder
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Check if it's a file
#         if os.path.isfile(file_path):
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 lines = file.readlines()

#             # Initialize an empty list to hold the modified lines
#             modified_lines = []
#             ne_counter = 1

#             # Find the maximum index in the second column
#             max_index = 0
#             for line in lines:
#                 stripped_line = line.strip()
#                 columns = stripped_line.split("\t")
#                 if len(columns) >= 2:
#                     try:
#                         # Convert second column to an integer if possible
#                         index = int(columns[1])
#                         max_index = max(max_index, index)
#                     except ValueError:
#                         # Ignore if the second column is not an integer
#                         continue
            
#             # Start the new index from max_index + 1
#             next_index = max_index + 1

#             # Process each line in the file
#             for line in lines:
#                 stripped_line = line.strip()
                
#                 # Skip lines starting with <sent_id=, #, or %
#                 if stripped_line.startswith("<sent_id=") or stripped_line.startswith("#") or stripped_line.startswith("%"):
#                     modified_lines.append(line)  # Retain these lines as-is
#                     continue

#                 # Split the line into columns
#                 columns = stripped_line.split("\t")
                
#                 # Check if the line has at least 3 columns
#                 if len(columns) >= 3:
#                     first_column = columns[0]
#                     second_column = columns[1]
#                     third_column = columns[2]
                                       
#                     # Check if the third column has (per, place, ne, org)
#                     if third_column in {"per", "place", "ne", "org"}:
#                         first_parts = first_column.split('+')
#                         for i, part in enumerate(first_parts):
#                             # Use "begin" for the first part and "inside" for subsequent parts
#                             tag_type = "begin" if i == 0 else "inside"
#                             modified_lines.append(f"{part}\t{next_index}\t-\t-\t-\t-\t-\t-\t{second_column}:{tag_type}\n")
#                             next_index += 1

#                         # Append the NE-tagged line
#                         modified_lines.append(f"[ne_{ne_counter}]\t{'\t'.join(columns[1:])}\n")
#                         ne_counter += 1
#                     else:
#                         # Append line without modification if third column is not a target tag
#                         modified_lines.append(line)
#                 else:
#                     # Append lines without modification if not enough columns
#                     modified_lines.append(line)

#             # Print or save the modified lines
#             print("".join(modified_lines))  # You can replace this with file writing logic

# # Replace 'your_folder_path' with the actual folder path containing your files
# folder_path = 'input/'
# process_files(folder_path)

import os

def process_files(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate over all files in the folder
    for file_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name)
        
        # Check if it's a file
        if os.path.isfile(input_file_path):
            with open(input_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Initialize an empty list to hold the modified lines
            modified_lines = []
            ne_counter = 1

            # Find the maximum index in the second column
            max_index = 0
            for line in lines:
                stripped_line = line.strip()
                columns = stripped_line.split("\t")
                if len(columns) >= 2:
                    try:
                        # Convert second column to an integer if possible
                        index = int(columns[1])
                        max_index = max(max_index, index)
                    except ValueError:
                        # Ignore if the second column is not an integer
                        continue
            
            # Start the new index from max_index + 1
            next_index = max_index + 1

            # Process each line in the file
            for line in lines:
                stripped_line = line.strip()
                
                # Skip lines starting with <sent_id=, #, or %
                if stripped_line.startswith("<sent_id=") or stripped_line.startswith("#") or stripped_line.startswith("%"):
                    modified_lines.append(line)  # Retain these lines as-is
                    continue

                # Split the line into columns
                columns = stripped_line.split("\t")
                
                # Check if the line has at least 3 columns
                if len(columns) >= 3:
                    first_column = columns[0]
                    second_column = columns[1]
                    third_column = columns[2]
                                       
                    # Check if the third column has (per, place, ne, org)
                    if third_column in {"per", "place", "ne", "org"}:
                        first_parts = first_column.split('+')
                        for i, part in enumerate(first_parts):
                            # Use "begin" for the first part and "inside" for subsequent parts
                            tag_type = "begin" if i == 0 else "inside"
                            modified_lines.append(f"{part}\t{next_index}\t-\t-\t-\t-\t-\t-\t{second_column}:{tag_type}\n")
                            next_index += 1

                        # Append the NE-tagged line
                        modified_lines.append(f"[ne_{ne_counter}]\t{'\t'.join(columns[1:])}\n")
                        ne_counter += 1
                    else:
                        # Append line without modification if third column is not a target tag
                        modified_lines.append(line)
                else:
                    # Append lines without modification if not enough columns
                    modified_lines.append(line)

            # Save the modified lines to the output folder
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(modified_lines)

# Replace 'input_folder_path' and 'output_folder_path' with actual folder paths
input_folder_path = '12/'
output_folder_path = '12_ne/'
process_files(input_folder_path, output_folder_path)
