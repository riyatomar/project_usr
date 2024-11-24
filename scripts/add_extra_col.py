def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_content = []
    within_sent_block = False
    for line in lines:
        # Check if line indicates the start of a sent_id block
        if line.startswith('<sent_id='):
            within_sent_block = True
            processed_content.append(line)
            continue
        elif within_sent_block and line.startswith('</sent_id>'):
            within_sent_block = False
            processed_content.append(line)
            continue
        
        # Skip % lines and directly add to processed content
        if line.startswith('%') or line.startswith('#'):
            processed_content.append(line)
            continue
        
        if within_sent_block:
            columns = line.strip().split('\t')
            
            # If the line already has 9 columns, keep it as-is
            if len(columns) == 9:
                processed_content.append(line)
            # If less than 9 columns, add hyphens to make it 9 columns
            elif len(columns) < 9:
                columns += ['-'] * (9 - len(columns))
                processed_content.append('\t'.join(columns) + '\n')
            # If more than 9 columns, skip the line (optional, depends on requirements)
            else:
                continue
        else:
            processed_content.append(line)

    # Write processed content back to a new file
    with open('processed_output.txt', 'w', encoding='utf-8') as output_file:
        output_file.writelines(processed_content)

# Call the function with the file path
process_file('input_file.txt')

