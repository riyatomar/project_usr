import re

# Open the file for reading
with open('input/2', 'r', encoding='utf-8') as file:
    lines = file.readlines()

updated_lines = []
ratio_count = 0
highest_index = 0
found_hash = False
ratios = []
ratio_dep_values = {}  # Dictionary to store ratio dependencies

# First loop: Find the rounded values, collect ratio counts, and find the highest index
for line in lines:
    if line.strip().startswith('#'):
        found_hash = True
        highest_index = 0  # Reset highest index after a hash line

    if not found_hash and '\t' in line:
        columns = line.split('\t')
        if len(columns) > 1:
            try:
                index = int(columns[1].strip())
                if index > highest_index:
                    highest_index = index
            except ValueError:
                pass

    if 'ratio:' in line:
        # Use regex to extract all ratios
        matches = re.findall(r'\[([0-9]+)\.([0-9]+)\/[0-9]+\.([0-9]+):', line)
        for match in matches:
            digit = int(match[0])
            decimal = int(match[1])
            rounded_value = str(round(digit + decimal / 10))
            ratios.append(rounded_value)
            ratio_count += 1  

    updated_lines.append(line)

# Second loop: Modify lines based on the ratios found
if ratios:
    final_lines = []
    index_map = {}  
    current_index = highest_index + 1
    
    for line in updated_lines:
        columns = line.split('\t')
        if len(columns) > 1 and columns[1].strip() in ratios:
            ratio_inx = columns[1].strip()
            index_map[ratio_inx] = current_index
            current_index += 2 

    updated_lines_with_indices = []
    for line in updated_lines:
        columns = line.split('\t')
        if len(columns) > 1 and columns[1].strip() in index_map:
            ratio_inx = columns[1].strip()
            new_index = index_map[ratio_inx]
            ratio_dep_val = columns[2:]  # Store dependency values
            ratio_dep_values[ratio_inx] = ratio_dep_val  # Save these values for later use
            updated_lines_with_indices.append(f"{columns[0].split(':')[0]}\t{new_index}\t-\t-\t-\t-\t-\t-\t{ratio_inx}:component1\n")
            updated_lines_with_indices.append(f"{columns[0].split(':')[1]}\t{new_index+1}\t-\t-\t-\t-\t-\t-\t{ratio_inx}:component2\n")  
        else:
            updated_lines_with_indices.append(line)
else:
    updated_lines_with_indices = updated_lines

# Third loop: Add [ratio_x] before the line starting with %
final_output = []
ratio_entries = {f"[ratio_{i+1}]": ratio for i, ratio in enumerate(ratios)}
for line in updated_lines_with_indices:
    if line.strip().startswith('%'):
        # Insert [ratio_x] entries before the line starting with %
        for i in range(1, ratio_count + 1):
            ratio_label = f"[ratio_{i}]"
            ratio_value = ratio_entries.get(ratio_label, '-')
            ratio_dep_val = ratio_dep_values.get(ratio_value, '-')  # Get the ratio dependency values
            final_out = ratio_label + '\t' + ratio_value + '\t' + '\t'.join(ratio_dep_val)
            final_output.append(final_out)
    final_output.append(line)

# Write the final lines back to the file
with open('output/2', 'w', encoding='utf-8') as file:
    file.writelines(final_output)
