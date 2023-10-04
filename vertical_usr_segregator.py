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

    # Split the input_text into segments using the "vertical" marker
    segments = re.split(r'vertical_', input_text)

    # Process the segments to create files
    for segment in segments[1:]:
        # Split the segment into lines
        lines = segment.strip().split('\n')

        # Get the filename from the first line
        filename = lines[0].strip()

        # Get the content by joining the remaining lines
        content = '\n'.join(lines[1:])

        # Create the output file path
        output_filepath = os.path.join(output_folder, filename)

        # Write the content to the file
        with open(output_filepath, 'w', encoding='utf-8') as file:
            file.write(content)

    print("Files created successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    sys.exit(1)
