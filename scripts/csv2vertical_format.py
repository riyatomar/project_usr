import os
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py input_folder output_folder")
    sys.exit(1)

input_folder = sys.argv[1]
output_folder = sys.argv[2]

# Ensure that the output folder exists or create it
os.makedirs(output_folder, exist_ok=True)

# List all files in the input folder
input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

for input_file in input_files:
    # Construct input and output file paths
    input_file_path = os.path.join(input_folder, input_file)
    output_file_path = os.path.join(output_folder, f"{input_file}")

    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    lines = input_text.strip().split('\n')
    parsed_rows = []

    transposed_data = [[] for _ in range(len(lines))]

    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(lines[0] + '\n')

            # Process and write the first 9 lines (or fewer if there are fewer lines)
            for i, line in enumerate(lines[1:9], start=1):
                values = line.split(',')
                values = [value.strip() if value else "-" for value in values]
                parsed_rows.append(values)

                # Transpose the values into the appropriate lists
                for j, value in enumerate(values):
                    if len(transposed_data) <= j:
                        transposed_data.append([])  # Add a new list if needed
                    transposed_data[j].append(value)

            # Remove empty rows from transposed data
            transposed_data = [row for row in transposed_data if any(row)]

            # Write the transposed data to the output file
            for row in transposed_data:
                output = "\t".join(row)
                output_file.write(output + '\n')

            # Write the remaining lines after processing the first 9 (or fewer) lines
            for line in lines[1 + len(parsed_rows):]:
                output_file.write(line + '\n')

    except IndexError:
        # Handle the IndexError by skipping the current file and continue to the next file
        print(f"Error processing file {input_file}")
        continue
