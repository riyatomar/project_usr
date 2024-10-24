import sys
import os

def process_file(file_path, output_folder):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False

    # Split the text into lines using split('\n')
    lines = input_text.split('\n')

    # Collect the lines in a list
    collected_lines = []
    for line in lines[2:]:
        if "tive" in line:
            break
        collected_lines.append(line)

    # Transpose the collected lines
    transposed_lines = list(zip(*[line.split() for line in collected_lines]))

    output_filename = os.path.splitext(os.path.basename(file_path))[0] #+ "_output.txt"
    output_filepath = os.path.join(output_folder, output_filename)

    try:
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            for line in lines[:2]:
                output_file.write(line + '\n')
            # Print the transposed lines
            for i, transposed_line in enumerate(transposed_lines):
                if i == 0:
                    output_format = ",".join(transposed_line)
                else:
                    output_format = ",".join(transposed_line).replace('-', '')
                output_file.write(output_format + '\n')
            # Print all the lines after the transposed lines
            for line in lines[len(collected_lines) + 2:]:

                output_file.write(line + '\n')
    except IOError as e:
        print(f"Error: Failed to write to '{output_filepath}': {str(e)}")
        return False

    return True

def main():
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_folder output_folder")
        sys.exit(1)

    # Get the input and output folders from the command-line arguments
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Check if the input folder exists
    if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' not found.")
        sys.exit(1)

    # Check if the output folder exists, create it if it doesn't
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError as e:
            print(f"Error: Failed to create output folder '{output_folder}': {str(e)}")
            sys.exit(1)

    # List all files in the input folder
    file_list = os.listdir(input_folder)

    # Process each file in the folder
    for file_name in file_list:
        # if file_name.endswith(".txt"):  # Process only .txt files
        file_path = os.path.join(input_folder, file_name)
        success = process_file(file_path, output_folder)
        if success:
            print(f"File '{file_path}' processed successfully.")

    print("Processing complete.")

if __name__ == "__main__":
    main()
