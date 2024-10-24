import os
import sys
import re

def first_line_starts_with_sent_id(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        first_line = file.readline().strip()
        return first_line.startswith("<sent_id=")

def last_line_ends_with_sent_id(file_path, const_list):
    with open(file_path, 'r', encoding="utf-8") as file:
        last_line = None
        prev_line = None
        for line in file:
            prev_line = last_line
            last_line = line.strip()
        if prev_line and last_line.endswith("</sent_id>"):
            for keyword in const_list:
                if prev_line.startswith("*" + keyword):
                    return True
        return False

def second_line_starts_with_single_hash(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        first_line = next(file).strip()  # Skip the first line
        second_line = next(file).strip()  # Read the second line
        return second_line.startswith("#")

def check_8_columns_after_second_line(file_path, skip_keywords, pronoun_list, const_list, output_file):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            # Skip the first two lines
            next(file)
            next(file)

            for line in file:
                line_content = line.strip()
                if any(keyword in line_content.lower() for keyword in skip_keywords):
                    if not line_content.startswith('%'):
                        print(f"{file_path} \t Sentence type should start with '%'.", file=output_file)
                    break  # Stop checking if any skip_keyword is found
                columns = re.split(r'\s+', line_content)

                if columns[0] in pronoun_list:
                    if not line_content.startswith("$"):
                        print(f"{file_path} \t Pronoun {columns[0]} should start with '$'.", file=output_file)

                if all(column != '-' for column in [columns[0], columns[1], columns[4]]):
                    if len(columns) != 8:
                        print(f"{file_path} \t Row starting with {columns[0]} concept, does not contain 8 columns information.", file=output_file)
                    column5_parts = columns[4].split(":")
                    if len(column5_parts) == 2 and column5_parts[0].isdigit() and column5_parts[1].isalnum():
                        pass 
                    else:
                        print(f"{file_path} \t Row starting with {columns[0]} concept, does not have correct information in Column 5 .", file=output_file)
                else:
                    print(f"{file_path} \t Row starting with {columns[0]} concept, should not contain only hyphens in columns 1, 2, and 5.", file=output_file)

    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=output_file)

def process_files(folder_path, output_file_path, skip_keywords, pronoun_list, const_list):
    with open(output_file_path, 'w', encoding="utf-8") as output_file:
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)

                if os.path.isfile(file_path):
                    try:
                        starts_with_sent_id = first_line_starts_with_sent_id(file_path)
                        ends_with_sent_id = last_line_ends_with_sent_id(file_path, const_list)
                        second_line_single_hash = second_line_starts_with_single_hash(file_path)

                        with open(file_path, 'r', encoding="utf-8") as file:
                            file_content = file.read().lower()

                        skip_keywords_present = any(keyword in file_content for keyword in skip_keywords)

                        if not starts_with_sent_id:
                            print(f"{file_path} \t The first line does not start with '<sent_id='.", file=output_file)

                        if not ends_with_sent_id:
                            print(f"{file_path} \t The last line does not end with '</sent_id>' or construction info is incorrect", file=output_file)

                        if not second_line_single_hash:
                            print(f"{file_path} \t The second line does not start with hash (#).", file=output_file)

                        check_8_columns_after_second_line(file_path, skip_keywords, pronoun_list, const_list, output_file)

                    except UnicodeDecodeError as e:
                        print(f"Error reading {filename}: {e}", file=output_file)
        else:
            print(f"The folder '{folder_path}' does not exist or is not a directory.", file=output_file)

def sort_lines_by_first_column(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        
        sorted_lines = sorted(lines, key=lambda line: line.split('\t')[0])
        
        with open(output_file_path, 'w') as file:
            file.writelines(sorted_lines)
        
        print("Sorting completed successfully. Output written to", output_file_path)
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # Code 1 configuration
    folder_path = sys.argv[1]  # input folder
    output_file_path = "format_error.tsv"  # output file path

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
        "sent_id"]

    const_list = ["span", "nil", "conj", "disjunct", "calender", "early_late", "meas",
                "disjunction", "time_meas", "dist_meas", "mass_meas", "length_meas",
                "rate", "fraction", "compound"]

    pronoun_list = ["wyax", "yax", "speaker", "addressee", "kim"]

    # Run Code 1
    process_files(folder_path, output_file_path, skip_keywords, pronoun_list, const_list)

    # Code 2 configuration
    input_file_path = output_file_path
    # output_sorted_file_path = "error_file.tsv"

    # Run Code 2
    sort_lines_by_first_column(input_file_path, output_file_path)
