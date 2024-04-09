import os
import sys

folder_path = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, "w", encoding="utf-8") as output:
    output.write("keywords\tsentence\tsent_ID\n")

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

                if len(lines) >= 2:
                    second_line = lines[1].strip()
                    substrings_to_check = [",hE_1", "+hE_1", ",ho_1", "+ho_1"]

                    values_to_print = []
                    for value in second_line.split(","):
                        if any(substring in value for substring in substrings_to_check):
                            values_to_print.append(value.strip())

                    if values_to_print:
                        first_line = lines[0].strip()
                        output.write(f"{', '.join(values_to_print)}\t{first_line}\t{filename}\n")

print("Processing completed")
