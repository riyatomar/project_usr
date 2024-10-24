import os

def extract_highest_index(lines):
    highest_index = -1  # Initialize to -1 to handle cases where no valid index is found
    
    for line in lines:
        line = line.rstrip()  # Remove trailing newlines
        # Skip lines that don't contain tab-separated values
        if '\t' in line:
            parts = line.split('\t')
            # Ensure the line has at least two columns
            if len(parts) > 1:
                try:
                    # Extract the second column value
                    value = parts[1]
                    # Check if the value is a valid integer
                    index = int(value)
                    # Update highest_index if this value is greater
                    if index > highest_index:
                        highest_index = index
                except ValueError:
                    # Handle cases where the second column is not a valid integer
                    continue
    
    return highest_index

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extract the highest index from the second column
    highest_index = extract_highest_index(lines)

    processed_lines = []
    nc_counter = 1  # Initialize the counter for [nc_1], [nc_2], ...
    nc_index = highest_index + 1  # Initialize the index for nc_

    for line in lines:
        line = line.rstrip()  # Remove any trailing newlines
        if '+' in line and '#' not in line:
            # Split the line by '+' to get segments
            parts = line.split('+')
            print(parts)  # Debugging line to check parts
            # Process each segment
            for i, part in enumerate(parts):
                part = part.strip()  # Strip whitespace from each segment
                if part:  # Proceed only if part is not empty
                    try:
                        nc_part = part.split('\t')  # Split by tabs
                        # Ensure that we have enough columns
                        if len(nc_part) >= 8:
                            nc_inx = nc_part[1]  # Get the nc_inx
                            spk_info = nc_part[6]  # Assume speaker info is in the 7th column
                            
                            # Create processed lines for each segment
                            processed_lines.append(f"{parts[0]}_{i + 1}\t{nc_index}\t-\t-\t-\t-\t-\t-\t{nc_inx}:mod\n")
                            processed_lines.append(f"{nc_part[0]}\t{nc_index + 1}\t-\t-\t-\t-\t{spk_info}\t-\t{nc_inx}:head\n")
                            processed_lines.append(f"[nc_{nc_counter}]\t{nc_part[1]}\t{nc_part[2]}\t{nc_part[3]}\t{nc_part[4]}\t{nc_part[5]}\t-\t{nc_part[7]}\t-\n")
                            
                            nc_counter += 1  # Increment counter for [nc_1], [nc_2], etc.
                            nc_index += 2  # Increment nc_index by 2 for next parts
                    except IndexError:
                        processed_lines.append(line)
                        # print(f"Skipping line due to missing data: {line}")
                        continue
        else:
            processed_lines.append(line + '\n')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)

def process_files_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        try:
            process_file(input_file, output_file)
        except Exception as e:
            print(f"Skipping file {filename} due to an error: {e}")

input_folder = '/home/riya/project_usr/cp_outputs'
output_folder = '/home/riya/project_usr/comp_outputs'
process_files_in_folder(input_folder, output_folder)
