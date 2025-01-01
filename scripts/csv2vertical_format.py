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

# Define the skip keywords
skip_keywords = [
    "affirmative",
    "negative",
    "yn_interrogative",
    "interrogative",
    "imperative",
    "pass_affirmative",
    "pass_negative",
    "pass_interrogative",
    "pass_yn_interrogative",
    "fragment",
    "title",
    "heading",
    "term",
    "sent_id"
]

for input_file in input_files:
    # Construct input and output file paths
    input_file_path = os.path.join(input_folder, input_file)
    output_file_path = os.path.join(output_folder, f"{input_file}")

    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    lines = input_text.strip().split('\n')
    parsed_rows = []

    transposed_data = []

    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Write the first two lines as-is
            output_file.write(lines[0] + '\n' + lines[1] + '\n')

            # Process lines to segregate rows for transposition and skipped lines
            skipped_lines = []  # Store lines with skip keywords
            for line in lines[2:]:
                if any(keyword in line for keyword in skip_keywords):
                    skipped_lines.append(line)
                else:
                    values = line.split(',')
                    values = [value.strip() if value else "-" for value in values]
                    parsed_rows.append(values)

            # Transpose the collected rows
            for col_idx in range(len(parsed_rows[0])):
                transposed_row = [row[col_idx] if col_idx < len(row) else "-" for row in parsed_rows]
                transposed_data.append(transposed_row)

            # Write transposed data to the output file
            for row in transposed_data:
                output_file.write("\t".join(row) + '\n')

            # Write the skipped lines after the transposed data
            for line in skipped_lines:
                output_file.write(line + '\n')

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error processing file {input_file}: {e}")
        continue
