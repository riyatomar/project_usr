import os
import re
import glob

def process_file(input_path, output_path):
    # Open the file for reading
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = []
    meas_count = 0
    highest_index = 0
    found_hash = False
    ratios = []
    meas_dep_values = {}  # Dictionary to store ratio dependencies

    # First loop: Find the rounded values, collect ratio counts, and find the highest index
    for line in lines:
        if line.strip().startswith('#'):
            found_hash = True
            highest_index = 0  # Reset highest index after a hash line

        if '\t' in line:
            columns = line.split('\t')
            # print(columns)
            if len(columns) > 1:
                try:
                    index = int(columns[1].strip())
                    if index > highest_index:
                        highest_index = index
                        # print(highest_index)
                except ValueError:
                    pass

        if 'meas:' in line:
            # print('true')
            # Use regex to extract all ratios
            # matches = re.findall(r'\[([0-9]+)\.([0-9]+)\/[0-9]+\.([0-9]+):', line)
            matches = re.findall(r'\[([0-9]+)\.([0-9]+)@', line)
            for match in matches:
                # print('true')
                digit = int(match[0])
                decimal = int(match[1])
                rounded_value = str(round(digit + decimal / 10))
                ratios.append(rounded_value)
                meas_count += 1  

        updated_lines.append(line)

    # Second loop: Modify lines based on the ratios found
    if ratios:
        final_lines = []
        index_map = {}  
        current_index = highest_index + 1
        
        for line in updated_lines:
            columns = line.split('\t')
            if len(columns) > 1 and columns[1].strip() in ratios:
                meas_inx = columns[1].strip()
                index_map[meas_inx] = current_index
                current_index += 2 

        updated_lines_with_indices = []
        for line in updated_lines:
            columns = line.split('\t')
            # print(columns)
            if len(columns) > 1 and columns[1].strip() in index_map:
                meas_inx = columns[1].strip()
                # print(meas_inx)
                new_index = index_map[meas_inx]
                unit_inx = new_index + 1
                meas_dep_val = columns[2:]  # Store dependency values
                meas_dep_values[meas_inx] = meas_dep_val  # Save these values for later use
                updated_lines_with_indices.append(f"{columns[0].split('+')[0]}\t{new_index}\t-\t-\t{unit_inx}:card\t-\t-\t-\t{meas_inx}:count\n")
                updated_lines_with_indices.append(f"{columns[0].split('+')[1]}\t{new_index+1}\t-\t-\t-\t-\t-\t-\t{meas_inx}:unit\n")  
            else:
                updated_lines_with_indices.append(line)
    else:
        updated_lines_with_indices = updated_lines

    # Third loop: Add [meas_x] before the line starting with %
    final_output = []
    meas_entries = {f"[meas_{i+1}]": ratio for i, ratio in enumerate(ratios)}
    for line in updated_lines_with_indices:
        if line.strip().startswith('%'):
            # Insert [meas_x] entries before the line starting with %
            for i in range(1, meas_count + 1):
                meas_label = f"[meas_{i}]"
                meas_value = meas_entries.get(meas_label, '-')
                meas_dep_val = meas_dep_values.get(meas_value, '-')  # Get the ratio dependency values
                final_out = meas_label + '\t' + meas_value + '\t' + '\t'.join(meas_dep_val)
                final_output.append(final_out)
        final_output.append(line)

    # Write the final lines back to the file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(final_output)

def process_all_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for input_file in glob.glob(os.path.join(input_folder, '*')):
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        process_file(input_file, output_file)

# Define your input and output folders
input_folder = 'ratio_outputs'
output_folder = 'meas_outputs'

# Process all files
process_all_files(input_folder, output_folder)
