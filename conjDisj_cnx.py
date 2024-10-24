# # import os
# # import re
# # import glob

# # def process_text(text):
# #     lines = text.strip().split('\n')
# #     content_lines = []
# #     conj_lines = []
# #     disjunct_lines = []
# #     other_lines = []
# #     percent_lines = []
# #     conj_indices = []
# #     disjunct_indices = []
# #     index_info = {}
# #     max_index = 0
# #     record_content = False
# #     sent_id_open = None
# #     sent_id_close = None
# #     asterisk_lines = []

# #     for line in lines:
# #         if line.startswith('<sent_id='):
# #             content_lines.append(line)
# #             sent_id_open = line
# #             record_content = False
# #             continue
# #         if line.startswith('</sent_id>'):
# #             sent_id_close = line
# #             record_content = False
# #             continue
# #         if line.startswith('#'):
# #             content_lines.append(line)
# #             record_content = True
# #             continue
# #         if line.startswith('%'):
# #             percent_lines.append(line)
# #             record_content = False
# #             continue
# #         if line.startswith('*'):
# #             asterisk_lines.append(line)
# #             conj_match = re.findall(r'conj:\[([^\]]+)\]', line)
# #             disjunct_match = re.findall(r'disjunct:\[([^\]]+)\]', line)
# #             other_match = re.findall(r'(compound:[^\]]+\])', line)
# #             for cm in conj_match:
# #                 conj_indices.append([int(x) for x in cm.split(',')])
# #             for dm in disjunct_match:
# #                 disjunct_indices.append([int(x) for x in dm.split(',')])
# #             for om in other_match:
# #                 other_lines.append(om)
# #             continue
# #         if record_content:
# #             match = re.search(r'\s+(\d+)\s+.*?\s+\S+\s+(\S+)\s+', line)
# #             if match:
# #                 index = int(match.group(1))
# #                 max_index = max(max_index, index)
# #                 sixth_column_info = match.group(2)
# #                 index_info[index] = sixth_column_info
# #             content_lines.append(line)

# #     next_index_conj = max_index + 1
# #     next_index_disjunct = next_index_conj + len(conj_indices)
# #     op_labels = {}
# #     conj_index = next_index_conj

# #     for indices in conj_indices:
# #         for idx, i in enumerate(indices):
# #             op_labels[i] = f"\t{conj_index}:op{idx + 1}"
# #             # print(op_labels[i])
# #         conj_index += 1

# #     disjunct_index = next_index_conj + len(conj_indices)
# #     for indices in disjunct_indices:
# #         for idx, i in enumerate(indices):
# #             op_labels[i] = f"\t{disjunct_index}:op{idx + 1}"
# #         disjunct_index += 1

# #     final_lines = []
# #     for line in content_lines:
# #         # print(content_lines)
# #         match = re.search(r'\s+(\d+)\s+', line)
# #         if match:
# #             index = int(match.group(1))
# #             # print(index)
# #             if index in op_labels:
# #                 # print(op_labels)
# #                 line += f' {op_labels[index]}'
# #                 parts = line.split()
# #                 # parts[4] = '-'
# #                 parts.pop(4)
# #                 line = '\t'.join(parts)
# #                 # print(line)
# #         if line.startswith('<sent_id=') or line.startswith('#'):
# #             final_lines.append(line)
# #         else:
# #             columns = line.split()
# #             while len(columns) < 9:
# #                 columns.append('-')
# #             final_lines.append('\t'.join(columns))

# #     for i, conj in enumerate(conj_indices):
# #         first_conj_index = conj[0]
# #         conj_info = index_info.get(first_conj_index, '-')
# #         conj_lines.append(f"[conj_{i + 1}]\t{next_index_conj + i}\t-\t-\t{conj_info}\t-\t-\t-\t-")
    
# #     for i, disj in enumerate(disjunct_indices):
# #         first_disjunct_index = disj[0]
# #         disjunct_info = index_info.get(first_disjunct_index, '-')
# #         disjunct_lines.append(f"[disjunct_{i + 1}]\t{next_index_disjunct + i}\t-\t-\t{disjunct_info}\t-\t-\t-\t-")

# #     final_lines.extend(conj_lines)
# #     final_lines.extend(disjunct_lines)
    
# #     if percent_lines:
# #         final_lines.extend(percent_lines)
        
# #     if asterisk_lines:
# #         final_lines.extend(asterisk_lines)
        
# #     if sent_id_close:
# #         final_lines.append(sent_id_close)

# #     if other_lines:
# #         final_lines.append(' '.join(other_lines))

# #     return final_lines

# # def process_files(input_folder, output_folder):
# #     input_files = glob.glob(os.path.join(input_folder, '*'))
    
# #     if not os.path.exists(output_folder):
# #         os.makedirs(output_folder)

# #     for input_file in input_files:
# #         with open(input_file, 'r', encoding='utf-8') as infile:
# #             text = infile.read()

# #         content = process_text(text)

# #         output_file = os.path.join(output_folder, os.path.basename(input_file))
        
# #         with open(output_file, 'w', encoding='utf-8') as outfile:
# #             for line in content:
# #                 if line.startswith('<sent_id='):# or line.startswith('#'):
# #                     outfile.write(line + '\n')
# #                 else:
# #                     outfile.write(line + '\n')

# # input_folder = 'meas_outputs'
# # output_folder = '/home/riya/project_usr/final_outputs'
# # process_files(input_folder, output_folder)

# import os
# import re
# import glob

# def process_text(text):
#     lines = text.strip().split('\n')
#     content_lines = []
#     conj_lines = []
#     disjunct_lines = []
#     other_lines = []
#     percent_lines = []
#     conj_indices = []
#     disjunct_indices = []
#     index_info = {}
#     max_index = 0
#     record_content = False
#     sent_id_open = None
#     sent_id_close = None
#     asterisk_lines = []

#     for line in lines:
#         if line.startswith('<sent_id='):
#             content_lines.append(line)
#             sent_id_open = line
#             record_content = False
#             continue
#         if line.startswith('</sent_id>'):
#             sent_id_close = line
#             record_content = False
#             continue
#         if line.startswith('#'):
#             content_lines.append(line)
#             record_content = True
#             continue
#         if line.startswith('%'):
#             percent_lines.append(line)
#             record_content = False
#             continue
#         if line.startswith('*'):
#             asterisk_lines.append(line)
#             conj_match = re.findall(r'conj:\[([^\]]+)\]', line)
#             # print(conj_match)
#             disjunct_match = re.findall(r'disjunct:\[([^\]]+)\]', line)
#             other_match = re.findall(r'(compound:[^\]]+\])', line)
#             for cm in conj_match:
#                 # Check and split only valid integers, ignore empty or invalid values
#                 # indices = [x for x in cm.split(',') if x.isdigit()]
#                 indices = [x.strip() for x in cm.split(',') if x.isdigit()]
#                 if indices:
#                     print(indices)
#                     conj_indices.append([int(x) for x in indices])
#             for dm in disjunct_match:
#                 indices = [x for x in dm.split(',') if x.isdigit()]
#                 if indices:
#                     disjunct_indices.append([int(x) for x in indices])
#             for om in other_match:
#                 other_lines.append(om)
#             continue
#         if record_content:
#             match = re.search(r'\s+(\d+)\s+.*?\s+\S+\s+(\S+)\s+', line)
#             if match:
#                 index = int(match.group(1))
#                 max_index = max(max_index, index)
#                 sixth_column_info = match.group(2)
#                 index_info[index] = sixth_column_info
#             content_lines.append(line)

#     next_index_conj = max_index + 1
#     next_index_disjunct = next_index_conj + len(conj_indices)
#     op_labels = {}
#     conj_index = next_index_conj

#     for indices in conj_indices:
#         # print(indices)
#         for idx, i in enumerate(indices):
#             # print(idx, i)
#             op_labels[i] = f"\t{conj_index}:op{idx + 1}"
#         conj_index += 1

#     disjunct_index = next_index_conj + len(conj_indices)
#     for indices in disjunct_indices:
#         for idx, i in enumerate(indices):
#             op_labels[i] = f"\t{disjunct_index}:op{idx + 1}"
#         disjunct_index += 1

#     final_lines = []
#     for line in content_lines:
#         match = re.search(r'\s+(\d+)\s+', line)
#         if match:
#             index = int(match.group(1))
#             if index in op_labels:
#                 line += f' {op_labels[index]}'
#                 parts = line.split()
#                 parts.pop(4)
#                 line = '\t'.join(parts)
#         if line.startswith('<sent_id=') or line.startswith('#'):
#             final_lines.append(line)
#         else:
#             columns = line.split()
#             while len(columns) < 9:
#                 columns.append('-')
#             final_lines.append('\t'.join(columns))

#     for i, conj in enumerate(conj_indices):
#         first_conj_index = conj[0]
#         # print(first_conj_index)
#         conj_info = index_info.get(first_conj_index, '-')
#         conj_lines.append(f"[conj_{i + 1}]\t{next_index_conj + i}\t-\t-\t{conj_info}\t-\t-\t-\t-")
    
#     for i, disj in enumerate(disjunct_indices):
#         first_disjunct_index = disj[0]
#         disjunct_info = index_info.get(first_disjunct_index, '-')
#         disjunct_lines.append(f"[disjunct_{i + 1}]\t{next_index_disjunct + i}\t-\t-\t{disjunct_info}\t-\t-\t-\t-")

#     final_lines.extend(conj_lines)
#     final_lines.extend(disjunct_lines)
    
#     if percent_lines:
#         final_lines.extend(percent_lines)
        
#     if asterisk_lines:
#         final_lines.extend(asterisk_lines)
        
#     if sent_id_close:
#         final_lines.append(sent_id_close)

#     if other_lines:
#         final_lines.append(' '.join(other_lines))

#     return final_lines

# def process_files(input_folder, output_folder):
#     input_files = glob.glob(os.path.join(input_folder, '*'))
    
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     for input_file in input_files:
#         try:
#             with open(input_file, 'r', encoding='utf-8') as infile:
#                 text = infile.read()

#             content = process_text(text)

#             output_file = os.path.join(output_folder, os.path.basename(input_file))
            
#             with open(output_file, 'w', encoding='utf-8') as outfile:
#                 for line in content:
#                     if line.startswith('<sent_id='):
#                         outfile.write(line + '\n')
#                     else:
#                         outfile.write(line + '\n')
#         except Exception as e:
#             print(f"Skipping file {input_file} due to error: {e}")

# # input_folder = 'meas_outputs'
# # output_folder = '/home/riya/project_usr/final_outputs'
# input_folder = 'input'
# output_folder = '/home/riya/project_usr/output'
# process_files(input_folder, output_folder)


import os
import re
import glob

def process_text(text):
    lines = text.strip().split('\n')
    content_lines = []
    conj_lines = []
    disjunct_lines = []
    other_lines = []
    percent_lines = []
    conj_indices = []
    disjunct_indices = []
    index_info = {}
    max_index = 0
    record_content = False
    sent_id_open = None
    sent_id_close = None
    asterisk_lines = []

    for line in lines:
        if line.startswith('<sent_id='):
            content_lines.append(line)
            sent_id_open = line
            record_content = False
            continue
        if line.startswith('</sent_id>'):
            sent_id_close = line
            record_content = False
            continue
        if line.startswith('#'):
            content_lines.append(line)
            record_content = True
            continue
        if line.startswith('%'):
            percent_lines.append(line)
            record_content = False
            continue
        if line.startswith('*'):
            asterisk_lines.append(line)
            conj_match = re.findall(r'conj:\[([^\]]+)\]', line)
            disjunct_match = re.findall(r'disjunct:\[([^\]]+)\]', line)
            other_match = re.findall(r'(compound:[^\]]+\])', line)
            for cm in conj_match:
                conj_indices.append([int(x) for x in cm.split(',')])
            for dm in disjunct_match:
                disjunct_indices.append([int(x) for x in dm.split(',')])
            for om in other_match:
                other_lines.append(om)
            continue
        if record_content:
            match = re.search(r'\s+(\d+)\s+.*?\s+\S+\s+(\S+)\s+', line)
            if match:
                index = int(match.group(1))
                max_index = max(max_index, index)
                sixth_column_info = match.group(2)
                index_info[index] = sixth_column_info
            content_lines.append(line)

    next_index_conj = max_index + 1
    next_index_disjunct = next_index_conj + len(conj_indices)
    op_labels = {}
    conj_index = next_index_conj

    for indices in conj_indices:
        for idx, i in enumerate(indices):
            op_labels[i] = f"\t-\t{conj_index}:op{idx + 1}"
            # print(op_labels[i])
        conj_index += 1

    disjunct_index = next_index_conj + len(conj_indices)
    for indices in disjunct_indices:
        for idx, i in enumerate(indices):
            op_labels[i] = f"\t-\t{disjunct_index}:op{idx + 1}"
        disjunct_index += 1

    final_lines = []
    for line in content_lines:
        # print(content_lines)
        match = re.search(r'\s+(\d+)\s+', line)
        if match:
            index = int(match.group(1))
            # print(index)
            if index in op_labels:
                # print(op_labels)
                line += f' {op_labels[index]}'
                parts = line.split()
                # parts[4] = '-'
                parts.pop(4)
                line = '\t'.join(parts)
                # print(line)
        if line.startswith('<sent_id=') or line.startswith('#'):
            final_lines.append(line)
        else:
            columns = line.split()
            print(columns)
            while len(columns) < 9:
                columns.append('-')
            final_lines.append('\t'.join(columns))

    for i, conj in enumerate(conj_indices):
        first_conj_index = conj[0]
        conj_info = index_info.get(first_conj_index, '-')
        # print('------------', conj_info)
        conj_lines.append(f"[conj_{i + 1}]\t{next_index_conj + i}\t-\t-\t{conj_info}\t-\t-\t-\t-")
    
    for i, disj in enumerate(disjunct_indices):
        first_disjunct_index = disj[0]
        disjunct_info = index_info.get(first_disjunct_index, '-')
        disjunct_lines.append(f"[disjunct_{i + 1}]\t{next_index_disjunct + i}\t-\t-\t{disjunct_info}\t-\t-\t-\t-")

    final_lines.extend(conj_lines)
    final_lines.extend(disjunct_lines)
    
    if percent_lines:
        final_lines.extend(percent_lines)
        
    if asterisk_lines:
        final_lines.extend(asterisk_lines)
        
    if sent_id_close:
        final_lines.append(sent_id_close)

    if other_lines:
        final_lines.append(' '.join(other_lines))

    return final_lines

def process_files(input_folder, output_folder):
    input_files = glob.glob(os.path.join(input_folder, '*'))
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as infile:
            text = infile.read()

        content = process_text(text)

        output_file = os.path.join(output_folder, os.path.basename(input_file))
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in content:
                if line.startswith('<sent_id=') or line.startswith('#'):
                    outfile.write(line + '\n')
                else:
                    outfile.write(line + '\n')

# input_folder = 'input'
# output_folder = '/home/riya/project_usr/output'


input_folder = 'meas_outputs'
output_folder = '/home/riya/project_usr/final_outputs'
process_files(input_folder, output_folder)