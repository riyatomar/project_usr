import os
import re

# meas = ['sIDZiyAz', 'sekaMda', 'varga', 'mItara', 'varga', 'seMtImItara', 'hekteyara', 
#              'ekadZa', 'maMjileM']
# temp_meas = ['selsiyasa', 'PZerenahAita', 'kelvina']
# time_meas = ['minata', 'GaMtA', 'xina', 'sapwAha', 'mahInA', 'sAla']
# weight_meas = ["kilo", 'lItara', 'milIlItara', 'kilolItara', 'grAma', 'kilogrAma', 'milIgrAma', 'tana']
# length_meas = ["kilomItara", "mItara", "seMtImItara", "milImItara"]

time_meas = ['GaMtA', 'minita',  'sekenda', 'xina', 'hapwA', 'mAhinA', 'sAla']
dist_meas = ['mitara', 'sentimitara', 'kilomitara', 'milimitara', 'lAita iyAra', 'mAila']
weight_meas = ['grAma', 'kilogrAma', 'miligrAma', 'kuintAla', 'tana', 'Aunsa','pAunda','kArata', 'kilo']
length_meas = ['phita', 'inca', 'mAila','iYArda']
temp_meas = ['digra' 'PArenAhAita', 'digri' 'selasiyAsa', 'kelaBina', 'digri sentigreda']
width_meas = ['milimitara']
volume_meas = ['litara', 'gYAlona', 'pinta', 'kiubika mitara','kiubika sentimitara']

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
                if '+' in string_to_check:
                    # Split the string and process
                    plus_index = string_to_check.index('+')
                    part1 = string_to_check[:plus_index + 1].strip('+')  # Part before and including '+'
                    part2 = string_to_check[plus_index + 1:]  # Part after '+'
                    print(part2, '----------------')

                    # Check if the last part (after the '+') is in the meas_list
                    if any(part2 in lst for lst in (time_meas, dist_meas, length_meas)):
                        if len(columns) > 1 and columns[1].strip().isdigit():
                            meas_cnx_idx = int(columns[1].strip())
                            if part2 in meas:
                                meas_cnx = '[meas_1]' + '\t' + "\t".join(columns[1:])
                            elif part2 in temp_meas:
                                meas_cnx = '[temp_meas_1]' + '\t' + "\t".join(columns[1:])
                            elif part2 in weight_meas:
                                print('trueeeeeeeeeeeeeeeee')
                                meas_cnx = '[weight_meas_1]' + '\t' + "\t".join(columns[1:])
                            # Output the part before '+' with count and the part after '+' with unit
                            output_lines.append(f"{part1}\t{meas_cnx_idx + 1}\t-\t-\t-\t-\t-\t-\t{meas_cnx_idx}:count")
                            output_lines.append(f"{part2}\t{meas_cnx_idx + 2}\t-\t-\t-\t-\t-\t-\t{meas_cnx_idx}:unit")
                            output_lines.append(meas_cnx)
                        else:
                            output_lines.append(line.strip())
                    else:
                        output_lines.append(line.strip())
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
