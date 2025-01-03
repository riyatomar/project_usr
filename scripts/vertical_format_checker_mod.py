import os, sys, re

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
            seen_indices = set()

            for line in file:
                line_content = line.strip()
                if any(keyword in line_content.lower() for keyword in skip_keywords):
                    if not line_content.startswith('%'):
                        print(f"{file_path} \t Sentence type should start with '%'.", file=output_file)
                    break  # Stop checking if any skip_keyword is found
                columns = re.split(r'\s+', line_content)

                if len(columns) < 2:
                    continue  # Skip lines that don't have enough columns

                # Check if column[1] is a digit and unique
                if columns[1].isdigit():
                    if columns[1] in seen_indices:
                        print(f"{file_path} \t Index {columns[1]} in index column is repeated.", file=output_file)
                    else:
                        seen_indices.add(columns[1])
                else:
                    print(f"{file_path} \t {columns[0]} concept's index is incorrect. Found '{columns[1]}' as index.", file=output_file)


                if columns[0] in pronoun_list:
                    if not line_content.startswith("$"):
                        print(f"{file_path} \t Pronoun {columns[0]} should start with '$'.", file=output_file)

                if columns[0] == "$wyax":
                    if len(columns) < 7 or columns[6] not in ["proximal", "distal"]:
                        print(f"{file_path} \t Row with '$wyax' should have 'proximal' or 'distal' in column[6].", file=output_file)


                if all(column != '-' for column in [columns[0]]):
                    if len(columns) != 9:
                        print(f"{file_path} \t Row having concept {columns[0]} with index {columns[1]}, does not contain 9 columns information.", file=output_file)
                    column5_parts = columns[4].split(":")
                    if len(column5_parts) == 2 and column5_parts[0].isdigit() and column5_parts[1].isalnum():
                        pass 
                    elif '-' in column5_parts and columns[8] != '-' and re.match(r'^\d+:.+', columns[8]):
                        pass
                    else:
                        print(f"{file_path} \t Row starting with {columns[0]} concept has inccorect info in dependency or cnx column.", file=output_file)
                else:
                    print(f"{file_path} \t Inccorect info '{columns[0]}' in Column 1.", file=output_file)

    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=output_file)

def remove_double_hash_lines(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Write back lines that do not contain '##'
        with open(file_path, 'w', encoding="utf-8") as file:
            for line in lines:
                if '##' not in line:
                    file.write(line)
    except Exception as e:
        print(f"Error cleaning file {file_path}: {e}")

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
                            print(f"{file_path} \t The last line does not end with '</sent_id>'", file=output_file)

                        if not second_line_single_hash:
                            print(f"{file_path} \t The second line does not start with hash (#).", file=output_file)

                        check_8_columns_after_second_line(file_path, skip_keywords, pronoun_list, const_list, output_file)

                    except UnicodeDecodeError as e:
                        print(f"Error reading {filename}: {e}", file=output_file)
        else:
            print(f"The folder '{folder_path}' does not exist or is not a directory.", file=output_file)

    # Remove lines containing '##' from the output file
    remove_double_hash_lines(output_file_path)

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
