import re
import os

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

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split('\n\n')
    
def convert_lines_to_sublists(lines):
    return [line.split() for line in lines]

# def find_compound_line(lines):
#     for i, line in enumerate(lines):
#         if '*' in line and 'compound' in line:
#             return i, line
#     return None, None
def find_compound_line(lines, search_terms):
    for i, line in enumerate(lines):
        if '*' in line:
            for term in search_terms:
                if term in line:
                    return i, line, term
    return None, None, None



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

def replace_compound_line(lines, compound_index, replacement_value, count,search_term_value):
    # return f"{replacement_value}{count}]\t-\t-\t-\t-\t-\t-\t-\t-\n"
    return f"[{search_term_value}_{count}]\t-\t-\t-\t-\t-\t-\t-\t-\n"

def find_matching_index(new_lines, integer_part):
    return next((i for i, sublist in enumerate(new_lines) if len(sublist) > 1 and sublist[1] == integer_part), None)

def find_highest_index(data):
    max_index = -1
    for row in data:
        if len(row) > 1 and row[1].isdigit():
            index = int(row[1])
            if index > max_index:
                max_index = index
    return max_index

def modify_compound_line(j,ele1,index_five,max_index,new_compound_line,compound_list):
    print("here: ",new_compound_line)
    new_compound_line[1] = str(max_index + 1)
    if j!=0:
        new_compound_line[4] = index_five
    elif len(ele1)==1:
        new_compound_line[4] = index_five
    # new_compound_line.append()
    compound_list.append(new_compound_line)
    print("ccc:",compound_list)
    return new_compound_line

def modify_reference_lines(new_lines,matching_index,original_compound_list):
    print("modify function: ",new_lines[matching_index])
    if new_lines[matching_index] not in original_compound_list:
        original_compound_list.append(new_lines[matching_index])
    first_element = new_lines[matching_index][0]
    split_elements = first_element.split('+')
    print("split_elements: ",split_elements)
    return split_elements,matching_index,original_compound_list
    
    
def process_input_set(lines, any_part_count):
    
    # replacement_dict = {
    #     "r6": "[6-tat_",
    #     "samuccaya": "[xvanxa_",
    #     "k1": "[1-tat_",
    #     "k2": "[2-tat_",
    #     "k3": "[3-tat_",
    #     "k4": "[4-tat_",
    #     "k5": "[5-tat_",
    #     "k7": "[7-tat_",
    #     "-": "[compound_",
    #     "rt": "[4-tat_",
    #     "rh": "[3-tat_",
    #     "aBexa": "[karmaXAraya_"
    # }
    replacement_dict = {
        "r6": "[6-waw_",
        "samuccaya": "[xvanxa_",
        "k1": "[1-waw_",
        "k2": "[2-waw_",
        "k3": "[3-waw_",
        "k4": "[4-waw_",
        "k5": "[5-waw_",
        "k7": "[7-waw_",
        "-": "[compound_",
        "rt": "[4-waw_",
        "rh": "[3-waw_",
        "aBexa": "[karmaXAraya_"
    }
    split_elements=[]
    last_index_list = []
    match_list = []

    search_terms = [
    "3-waw", "4-waw", "5-waw", "6-waw", "7-waw", "naF-waw", "2-waw", 
    "karmaXAraya", "xvigu", "2-bahubrIhi", "3-bahubrIhi", "4-bahubrIhi", 
    "5-bahubrIhi", "6-bahubrIhi", "7-bahubrIhi", "xvanxva", 
    "avyayIBAva", "upapaxa", "maXyamapaxalopI", "compound"
    ]
    
    new_lines = convert_lines_to_sublists(lines)
    compound_index, compound_line, search_term_value = find_compound_line(lines,search_terms)
    print(search_term_value,"ssssssss")
    # print("ciiiiiiiii: ",compound_index)

    if compound_line:
        matches = extract_integer_and_any_part(compound_line)
        # print("abcd: ",matches)
        grouped = {}

        for item in matches:
            key = item[0]
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(item)

        # Convert the dictionary to the desired list of lists format
        result = [group for group in grouped.values()]


        print("res: ",result)
        for e,ele1 in enumerate(result):
            all_split_elements=[]
            compound_list = []
            original_compound_list = []
        # max_index = find_highest_index(new_lines)
            for j,match in enumerate(ele1):
                integer_part, any_part, full_any_part_left, full_any_part_right = match
                print("ap: ",any_part)

                if any_part in any_part_count:
                    any_part_count[any_part] += 1
                else:
                    any_part_count[any_part] = 1

                if any_part :
                    count = any_part_count[any_part]
                    # replacement_value = replacement_dict[any_part]
                    replacement_value = count

                    new_compound_line = replace_compound_line(lines, compound_index, replacement_value, count,search_term_value)
                    print("nc: ",new_compound_line)
                    new_compound_line = new_compound_line.split()
                    print("ncc:",new_compound_line)
                    matching_index = find_matching_index(new_lines, integer_part)
                    print("fbvkd: ",matching_index)
                    max_index = find_highest_index(new_lines)
                    if matching_index is not None:
                        index_five = new_lines[matching_index][4]
                    modified_compound_line = modify_compound_line(j,ele1,index_five,max_index,new_compound_line,compound_list)
                    print("modi: ",modified_compound_line)
                    new_lines.append(modified_compound_line)

                    split_elements,last_index,original_compound_list = modify_reference_lines(new_lines,matching_index,original_compound_list)
                    print("ooooooooo: ",original_compound_list)
                    if last_index not in last_index_list:
                        last_index_list.append(last_index)
                    
                    if split_elements not in all_split_elements:
                        all_split_elements.append(split_elements)
            
            new_lines=splited_elements(e,compound_list,new_lines,all_split_elements,last_index_list,original_compound_list,matches,result)
            remodify_compound_list(compound_list)
            # print("all: ",all_split_elements)
                

    return new_lines,any_part_count

def remodify_compound_list(compound_list):
    for i,ele in enumerate(compound_list):
        if i != 0 and len(compound_list[i - 1])<10:
            last_word=ele[1]+':'+'mod'
            compound_list[i-1].append(last_word)
    print(compound_list,"clllll: ")


def splited_elements(e,compound_list,new_lines,all_split_elements,last_index_list,original_compound_list,matches,result):
    print("lll: ",result)
    integer_part = ''
    any_part='' 
    full_any_part_left=''
    full_any_part_right = ''
    new_list=[]
    for j,split_element in enumerate(all_split_elements):
        n=0
        sub_list=[]
        last_index=last_index_list[e]
        
        matches.insert(0,matches[0])
        print(matches,'mtc')
        for i, (ele, match) in enumerate(zip(split_element, matches)):
            # print("ele: ",ele)
            integer_part, any_part, full_any_part_left, full_any_part_right = match
            if i == len(split_element)-1:
                high =find_highest_index(new_lines)
                # print("ele:",ele.split())
                ele+='\t-\t-\t-\t-\t-\t-\t-\t-\n'
                ele=ele.split()
                # ele[1]=str(int(new_lines[last_index_list[j]][1]))
                ele[1]=original_compound_list[j][1]
                print("AP: ",any_part)
                if any_part == "samuccaya":
                    mod_label, head_label = "op1", "op2"
                else:
                    mod_label, head_label = ("mod", "head") if any_part != "-" else (full_any_part_right, full_any_part_left)
                last_row=compound_list[j-1][1]+':'+ head_label
                ele.append(last_row)
                sub_list.append(ele)
                new_lines.insert(last_index+1,ele)
            else:
                # print(match,'match')
                high =find_highest_index(new_lines)
                # print("ele:",ele.split())
                ele+='\t-\t-\t-\t-\t-\t-\t-\t-\n'
                ele=ele.split()
                ele[1]=str(high+1)
                if any_part == "samuccaya":
                    mod_label, head_label = "op1", "op2"
                else:
                    mod_label, head_label = ("mod", "head") if any_part != "-" else (full_any_part_right, full_any_part_left)
                if i==0:
                    last_row=compound_list[j][1]+':'+mod_label
                    ele.append(last_row)
                else:
                    print("n is: ",n,i,compound_list)
                    last_row=compound_list[j][1]+':'+head_label
                    ele.append(last_row)
                sub_list.append(ele)
                new_lines.insert(last_index+1,ele)
            n+=1
            last_index=last_index+1
        new_list.append(sub_list)
        print('new lines',new_lines)

        for i,z in enumerate(new_lines):
            for j in original_compound_list:
                if z==j:
                    del new_lines[i]

    return new_lines

def main(input_folder_path, output_folder_path):
    for root, _, files in os.walk(input_folder_path):
        for file_name in files:
            input_file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(root, input_folder_path)
            output_file_dir = os.path.join(output_folder_path, relative_path)
            output_file_path = os.path.join(output_file_dir, file_name)
            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir)
            reorder_last_two_lines_in_place(input_file_path)
            print(file_name)
            all_input_sets = read_file(input_file_path)
            all_new_lines = []
            any_part_count = {}

            for input_set in all_input_sets:
                lines = input_set.strip().split('\n')
                new_lines, any_part_count = process_input_set(lines, any_part_count)
        
            with open(output_file_path, 'w', encoding='utf-8') as file:
                for string in new_lines:
                    if isinstance(string, list):
                        # Join the list into a single string with spaces
                        string = ' '.join(string)
                    file.write(string + '\n')
            reorder_specific_lines_at_end(output_file_path)
            ensure_four_hyphens(output_file_path)

    

if __name__ == "__main__":
    main("/home/riya/project_usr/sep", 'compound_outputs')