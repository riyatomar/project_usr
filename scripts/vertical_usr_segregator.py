import re
import sys
import os

try:
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        raise ValueError("Usage: python script.py input_file.txt output_folder")

    # Get the input file and output folder from the command-line arguments
    input_file = sys.argv[1]
    output_folder = sys.argv[2]

    # Check if the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    # Check if the output folder exists, create it if it doesn't
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read input text from the file
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Use regular expressions to find and extract the desired sections
    pattern = r'<sent_id=(.*?)</sent_id>'
    matches = re.finditer(pattern, input_text, re.DOTALL)

    for i, match in enumerate(matches):
        extracted_text = match.group(0)

        # Extract the text between "=" and ">"
        filename_match = re.search(r'<sent_id=(.*?)>', extracted_text)
        if filename_match:
            filename = filename_match.group(1)
        else:
            # Use a default filename if the pattern is not found
            filename = f"section_{i}"

        # Remove any invalid characters from the filename
        filename = re.sub(r'[\/:*?"<>|]', '', filename)

        # Write each extracted text to a new file in the output folder
        output_file_path = os.path.join(output_folder, f"{filename}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

    print(f"{i+1} sections segregated and saved into the output folder.")

except Exception as e:
    print(f"Error occurred: {e}")