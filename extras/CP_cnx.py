import os

def process_file(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    start_checking = False
    output_lines = []  # List to store lines to be written to the output file

    for line in lines:
        if line.startswith('#'):
            start_checking = True
            output_lines.append(line.strip())  # Append the line starting with #
            continue
        
        if start_checking:
            columns = line.strip().split()
            if len(columns) > 0:
                string_to_check = columns[0]
                if '+' in string_to_check and '-' in string_to_check:
                    # Split the string and process
                    plus_index = string_to_check.index('+')
                    part1 = string_to_check[:plus_index + 1].strip('+') + '_1'  # Part before and including '+'
                    part2 = string_to_check[plus_index + 1:]  # Part after '+'
                    
                    cp_cnx = '[cp_1]' + '\t' + "\t".join(columns[1:])
                    cp_cnx_idx = int(cp_cnx.split('\t')[1])
                    
                    output_lines.append(f"{part1}\t{cp_cnx_idx + 1}\t-\t-\t-\t-\t-\t-\t{cp_cnx_idx}:kriyAmUla")
                    output_lines.append(f"{part2}\t{cp_cnx_idx + 2}\t-\t-\t-\t-\t-\t-\t{cp_cnx_idx}:verbalizer")
                    output_lines.append(cp_cnx)
                else:
                    output_lines.append(line.strip())
            else:
                output_lines.append(line.strip())
        else:
            output_lines.append(line.strip())

    # Write the collected lines to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(output_lines) + '\n')

def process_files_in_folder(input_folder, output_folder):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path):
            # Define the path for the output file
            output_file_name = f"processed_{file_name}"
            output_file_path = os.path.join(output_folder, output_file_name)
            
            # Process the file and save the output
            process_file(file_path, output_file_path)

# Specify the paths to your input and output folders
input_folder = 'input'
output_folder = 'output'

process_files_in_folder(input_folder, output_folder)
