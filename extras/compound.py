import os
import re
import shutil

def reorder_last_two_lines_in_place(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    end_tag_index = None
    for i in range(len(lines)):
        if lines[i].strip() == "</sent_id>":
            end_tag_index = i
            break

    if end_tag_index is not None and end_tag_index >= 2:
        lines[end_tag_index - 2], lines[end_tag_index - 1] = lines[end_tag_index - 1], lines[end_tag_index - 2]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def reorder_specific_lines_at_end(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    content_lines = []
    special_lines = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("</sent_id>") or stripped_line.startswith("%") or stripped_line.startswith("*"):
            special_lines.append(line)
        else:
            content_lines.append(line)

    reordered_lines = content_lines + special_lines

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(reordered_lines)

def ensure_four_hyphens(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith("</sent_id>") or stripped_line.startswith("%fragment") or stripped_line.startswith("*compound"):
            modified_lines.append(line)
            continue

        columns = stripped_line.split()

        if len(columns) > 5:
            hyphen_count = len(columns) - 5
            if hyphen_count < 4:
                columns.extend(['-'] * (4 - hyphen_count))

        modified_line = '\t'.join(columns)
        modified_lines.append(modified_line.strip() + '\n')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

def find_highest_index(data):
    max_index = -1
    for row in data:
        if len(row) > 1 and row[1].isdigit():
            index = int(row[1])
            if index > max_index:
                max_index = index
    return max_index

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split('\n\n')

def find_compound_line(lines):
    for i, line in enumerate(lines):
        if '*' in line and 'compound' in line:
            return i, line
    return None, None

def extract_integer_and_any_part(compound_line):
    hyphenated_matches = re.findall(r'\[(\d+)\.\d+/\d+\.\d+:(\w+)-(\w+)\]', compound_line)
    non_hyphenated_matches = re.findall(r'\[(\d+)\.\d+/\d+\.\d+:(\w+)\]', compound_line)

    result = []
    for match in hyphenated_matches:
        integer_part, part1, part2 = match
        result.append((integer_part, '-', part1, part2))

    for match in non_hyphenated_matches:
        integer_part, any_part = match
        result.append((integer_part, any_part, any_part, any_part))

    return result

def replace_compound_line(lines, compound_index, replacement_value, count):
    return f"{replacement_value}{count}]\t-\t-\t-\t-\t-\t-\t-\t-\n"

def convert_lines_to_sublists(lines):
    return [line.split() for line in lines]

def find_matching_index(new_lines, integer_part):
    return next((i for i, sublist in enumerate(new_lines) if len(sublist) > 1 and sublist[1] == integer_part), None)

def update_sublists(new_lines, replacement_value, integer_part, index_five, compound_index, new_compound_line):
    for sublist in new_lines:
        if new_compound_line[0] in sublist[0]:
            sublist[4] = index_five

def create_new_sublists(split_elements, integer_part, new_lines, any_part):
    new_sublists = []
    mod_part, head_part = ("mod", "head") if any_part != "-" else ("mod", "head")

    for i, part in enumerate(split_elements):
        new_sublist = [part] + ['-'] * 9 + [f'0:{mod_part if i == 0 else head_part}']
        if i == 0:
            new_sublist[1] = "$$"
        elif i == 1:
            new_sublist[1] = integer_part
        new_sublists.append(new_sublist)

    return new_sublists

def find_no_of_compounds(comp_line):
    return comp_line.count("compound")

def process_input_set(lines, any_part_count):
    replacement_dict = {
        "r6": "[6-tat_",
        "samuccaya": "[xvanxa_",
        "k1": "[1-tat_",
        "k2": "[2-tat_",
        "k3": "[3-tat_",
        "k4": "[4-tat_",
        "k5": "[5-tat_",
        "k7": "[7-tat_",
        "-": "[compound_",
        "rt": "[4-tat_",
        "rh": "[3-tat_",
        "aBexa": "[karmaXAraya_"
    }

    new_lines = convert_lines_to_sublists(lines)
    compound_index, compound_line = find_compound_line(lines)

    if compound_line:
        matches = extract_integer_and_any_part(compound_line)
        for match in matches:
            integer_part, any_part, full_any_part_left, full_any_part_right = match

            if any_part in any_part_count:
                any_part_count[any_part] += 1
            else:
                any_part_count[any_part] = 1

            if any_part in replacement_dict:
                count = any_part_count[any_part]
                replacement_value = replacement_dict[any_part]

                new_compound_line = replace_compound_line(lines, compound_index, replacement_value, count)
                new_compound_line = new_compound_line.split()
                new_lines.append(new_compound_line)

                matching_index = find_matching_index(new_lines, integer_part)
                if matching_index is not None:
                    index_five = new_lines[matching_index][4]
                    update_sublists(new_lines, replacement_value, integer_part, index_five, compound_index, new_compound_line)

                    first_element = new_lines[matching_index][0]
                    if first_element.count('+') == 1:  # Check if there is exactly one "+"
                        split_elements = first_element.split('+')
                        new_sublists = create_new_sublists(split_elements, integer_part, new_lines, any_part)
                        new_lines.pop(matching_index)
                        new_lines[matching_index:matching_index] = new_sublists

    return new_lines, any_part_count

def process_file(input_file_path, output_file_path):
    try:
        reorder_last_two_lines_in_place(input_file_path)
        all_input_sets = read_file(input_file_path)
        all_new_lines = []
        any_part_count = {}

        for input_set in all_input_sets:
            lines = input_set.strip().split('\n')
            new_lines, any_part_count = process_input_set(lines, any_part_count)
            if new_lines:
                all_new_lines.append(new_lines)

        if not all_new_lines:
            return

        dup_lines = all_new_lines[0]

        joined_strings = ['\t'.join(sublist) for sublist in dup_lines]
        compound_index, compound_line = find_compound_line(joined_strings)

        if not compound_line:
            # Copy the file to the output folder if no compounds are found
            shutil.copy(input_file_path, output_file_path)
            return

        final_new_lines = convert_lines_to_sublists(joined_strings)

        dup_matches = extract_integer_and_any_part(compound_line)
        # new_index_val = final_new_lines[compound_index - 1][1]
        new_index_val = find_highest_index(final_new_lines)
        nc = find_no_of_compounds(compound_line)

        if nc >= 3:
        # Copy the input file to the output file as it is
            with open(input_file_path, 'r', encoding='utf-8') as infile:
                with open(output_file_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(infile.read())
            return

        for i, match in enumerate(dup_matches):
            integer_part = match[0]
            any_part = match[1]
            full_any_part_left = match[2]
            full_any_part_right = match[3]

            # mod_label, head_label = ("mod", "head") if any_part != "-" else (full_any_part_right, full_any_part_left)
            if any_part == "samuccaya":
                mod_label, head_label = "op1", "op2"

            else:
                mod_label, head_label = ("mod", "head") if any_part != "-" else (full_any_part_right, full_any_part_left)

            if nc == 2:
                final_new_lines[-2][1] = str(int(new_index_val) + 1)
                final_new_lines[-1][1] = str(int(new_index_val) + 2)

                matching_index = find_matching_index(final_new_lines, integer_part)
                final_new_lines[matching_index - 1][-1] = f"{final_new_lines[-2 + i][1]}:{mod_label}"
                final_new_lines[matching_index - 1][1] = str(int(new_index_val) + 3 + i)
                final_new_lines[matching_index][-1] = f"{final_new_lines[-2 + i][1]}:{head_label}"

            elif nc == 1:
                final_new_lines[-1][1] = str(int(new_index_val) + 1)

                matching_index = find_matching_index(final_new_lines, integer_part)
                final_new_lines[matching_index - 1][-1] = f"{final_new_lines[-1][1]}:{mod_label}"
                final_new_lines[matching_index - 1][1] = str(int(new_index_val) + 2)
                final_new_lines[matching_index][-1] = f"{final_new_lines[-1][1]}:{head_label}"

        joined_strings = ['\t'.join(map(str, sublist)) for sublist in final_new_lines]

        with open(output_file_path, 'w', encoding='utf-8') as file:
            for string in joined_strings:
                file.write(string + '\n')

        reorder_specific_lines_at_end(output_file_path)
        ensure_four_hyphens(output_file_path)

    except Exception as e:
        print(f"Error processing file {input_file_path}: {e}")

#If there are more than 1 "+" then the input is pasted as it is in the output
# def process_file(input_file_path, output_file_path):
#     try:
#         # Check if any line in the input file contains more than one "+"
#         with open(input_file_path, 'r', encoding='utf-8') as file:
#             lines = file.readlines()

#         # Early return if any line contains more than one "+"
#         if any(line.count('+') > 1 for line in lines):
#             shutil.copy(input_file_path, output_file_path)
#             return

#         reorder_last_two_lines_in_place(input_file_path)
#         all_input_sets = read_file(input_file_path)
#         all_new_lines = []
#         any_part_count = {}

#         for input_set in all_input_sets:
#             lines = input_set.strip().split('\n')
#             new_lines, any_part_count = process_input_set(lines, any_part_count)
#             if new_lines:
#                 all_new_lines.append(new_lines)

#         if not all_new_lines:
#             return

#         dup_lines = all_new_lines[0]

#         joined_strings = ['\t'.join(sublist) for sublist in dup_lines]
#         compound_index, compound_line = find_compound_line(joined_strings)

#         if not compound_line:
#             # Copy the file to the output folder if no compounds are found
#             shutil.copy(input_file_path, output_file_path)
#             return

#         final_new_lines = convert_lines_to_sublists(joined_strings)

#         dup_matches = extract_integer_and_any_part(compound_line)
#         new_index_val = final_new_lines[compound_index - 1][1]
#         nc = find_no_of_compounds(compound_line)

#         if nc >= 3:
#             # Copy the input file to the output file as it is
#             with open(input_file_path, 'r', encoding='utf-8') as infile:
#                 with open(output_file_path, 'w', encoding='utf-8') as outfile:
#                     outfile.write(infile.read())
#             return

#         for i, match in enumerate(dup_matches):
#             integer_part = match[0]
#             any_part = match[1]
#             full_any_part_left = match[2]
#             full_any_part_right = match[3]

#             if any_part == "samuccaya":
#                 mod_label, head_label = "op1", "op2"
#             else:
#                 mod_label, head_label = ("mod", "head") if any_part != "-" else (full_any_part_right, full_any_part_left)

#             if nc == 2:
#                 final_new_lines[-2][1] = str(int(new_index_val) + 1)
#                 final_new_lines[-1][1] = str(int(new_index_val) + 2)

#                 matching_index = find_matching_index(final_new_lines, integer_part)
#                 final_new_lines[matching_index - 1][-1] = f"{final_new_lines[-2 + i][1]}:{mod_label}"
#                 final_new_lines[matching_index - 1][1] = str(int(new_index_val) + 3 + i)
#                 final_new_lines[matching_index][-1] = f"{final_new_lines[-2 + i][1]}:{head_label}"

#             elif nc == 1:
#                 final_new_lines[-1][1] = str(int(new_index_val) + 1)

#                 matching_index = find_matching_index(final_new_lines, integer_part)
#                 final_new_lines[matching_index - 1][-1] = f"{final_new_lines[-1][1]}:{mod_label}"
#                 final_new_lines[matching_index - 1][1] = str(int(new_index_val) + 2)
#                 final_new_lines[matching_index][-1] = f"{final_new_lines[-1][1]}:{head_label}"

#         joined_strings = ['\t'.join(map(str, sublist)) for sublist in final_new_lines]

#         with open(output_file_path, 'w', encoding='utf-8') as file:
#             for string in joined_strings:
#                 file.write(string + '\n')

#         reorder_specific_lines_at_end(output_file_path)
#         ensure_four_hyphens(output_file_path)

#     except Exception as e:
#         print(f"Error processing file {input_file_path}: {e}")


def main(input_folder_path, output_folder_path):
    for root, _, files in os.walk(input_folder_path):
        for file_name in files:
            input_file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(root, input_folder_path)
            output_file_dir = os.path.join(output_folder_path, relative_path)
            output_file_path = os.path.join(output_file_dir, file_name)

            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir)

            process_file(input_file_path, output_file_path)
            if not os.path.exists(output_file_path):
                # Copy the file if it hasn't been processed
                shutil.copy(input_file_path, output_file_path)

if __name__ == "__main__":
    main('input', 'output_compound')
