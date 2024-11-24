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
    cp_counter = 1  # Initialize the counter for [cp_1], [cp_2], ...
    cp_index = highest_index + 1  # Initialize the index for cp_

    for line in lines:
        line = line.rstrip()  # Remove any trailing newlines
        if '+' in line and '#' not in line:
            parts = line.split('+')
            if len(parts) > 1:
                value_after_plus = parts[1].split('_')[0]
                if value_after_plus in {'ho', 'kara', 'le', 'xe', 'laga', 'lagA', 'dAla', 'raha', 'karanA', 'raKa', 'xenA', 'A', 'honA', 'lenA', 'laganA', 'lagAnA', 'dAlanA', 'rahanA', 'rakanA', 'kIjie', 'kA'}:
                    try:
                        cp_part = parts[1].strip('').split('\t')
                        spk_info = parts[1].strip('').split('\t')[6]
                        
                        if len(cp_part) > 1:
                            cp_inx = cp_part[1]
                            print(cp_part)
                            processed_lines.append(f"{parts[0]}_1\t{cp_index}\t-\t-\t-\t-\t-\t-\t{cp_inx}:kriyAmUla\n")
                            processed_lines.append(f"{cp_part[0]}\t{cp_index + 1}\t-\t-\t-\t-\t{spk_info}\t-\t{cp_inx}:verbalizer\n")
                            processed_lines.append(f"[cp_{cp_counter}]\t{cp_part[1]}\t{cp_part[2]}\t{cp_part[3]}\t{cp_part[4]}\t{cp_part[5]}\t-\t{cp_part[7]}\t-\n")
                            cp_counter += 1
                            cp_index += 2  # Increment cp_index by 2 for next parts
                            continue
                    except IndexError:
                        print(f"Skipping line due to missing data: {line}")
                        continue
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

input_folder = '/home/riya/project_usr/vertical/25_seg'
output_folder = '/home/riya/project_usr/cp_outputs'
# input_folder = '/home/riya/project_usr/input'
# output_folder = '/home/riya/project_usr/output'
process_files_in_folder(input_folder, output_folder)
