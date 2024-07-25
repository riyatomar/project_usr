import re

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

    for line in lines:
        if line.startswith('#'):
            content_lines.append(line)
            record_content = True
            continue
        if line.startswith('%'):
            percent_lines.append(line)
            record_content = False
            continue
        if line.startswith('*'):
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
            op_labels[i] = f"\t{conj_index}:op{idx + 1}"
        conj_index += 1

    disjunct_index = next_index_conj + len(conj_indices)
    for indices in disjunct_indices:
        for idx, i in enumerate(indices):
            op_labels[i] = f"\t{disjunct_index}:op{idx + 1}"
        disjunct_index += 1

    final_lines = []
    for line in content_lines:
        match = re.search(r'\s+(\d+)\s+', line)
        if match:
            index = int(match.group(1))
            if index in op_labels:
                line += f' {op_labels[index]}'
                parts = line.split()
                parts[4] = '-'
                line = '\t'.join(parts)

        columns = line.split()
        while len(columns) < 9:
            columns.append('-')
        final_lines.append('\t'.join(columns))

    for i, conj in enumerate(conj_indices):
        first_conj_index = conj[0]
        conj_info = index_info.get(first_conj_index, '-')
        conj_lines.append(f"[conj_{i + 1}]\t{next_index_conj + i}\t-\t-\t{conj_info}\t-\t-\t-\t-")
    
    for i, disj in enumerate(disjunct_indices):
        first_disjunct_index = disj[0]
        disjunct_info = index_info.get(first_disjunct_index, '-')
        disjunct_lines.append(f"[disjunct_{i + 1}]\t{next_index_disjunct + i}\t-\t-\t{disjunct_info}\t-\t-\t-\t-")

    final_lines.extend(conj_lines)
    final_lines.extend(disjunct_lines)
    final_lines.extend(percent_lines)

    if other_lines:
        final_lines.append(' '.join(other_lines))

    return final_lines

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()

    content = process_text(text)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in content:
            outfile.write(line + '\n')

input_file = '/home/riya/project_usr/input/1'
output_file = '/home/riya/project_usr/output/1'
main(input_file, output_file)
