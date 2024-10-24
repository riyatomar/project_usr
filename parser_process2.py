def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    geo_lines = []
    index_line_map = {}
    current_index = None

    # Store the content following each "Geo_ncert_" line
    for line in lines:
        if line.startswith("sent_id_"):
            current_index = line.strip()
            geo_lines.append(current_index)
            index_line_map[current_index] = []
        elif current_index:
            if line.strip():  # Only add non-empty lines
                index_line_map[current_index].append(line.strip())

    # Process each "Geo_ncert_" block
    for geo_line in geo_lines:
        print('\n')
        print(geo_line)
        line_mapping = {line.split('\t')[0]: line for line in index_line_map[geo_line]}  # Map index to line
        for line in index_line_map[geo_line]:
            columns = line.split('\t')
            if len(columns) > 6 and columns[7] == 'pof__cn':
                print(line)
                related_index = columns[6]
                if related_index in line_mapping:
                    print(line_mapping[related_index])

# Example usage
process_file('parser_out')
