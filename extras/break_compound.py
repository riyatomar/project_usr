def process_file(file_name):
    # Open and read the file
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    output = []
    inside_sent_id = False
    compound_counter = 1  # Counter for compound identifiers

    for line in data:
        line = line.strip()
        
        # Detecting start and end of a sentence
        if line.startswith('<sent_id'):
            inside_sent_id = True
            output.append(line)
            continue
        elif line.startswith('</sent_id>'):
            inside_sent_id = False
            output.append(f'[compound_{compound_counter}]')  # Add compound label before %affirmative
            output.append(line)
            compound_counter += 1
            continue
        
        # Processing content within <sent_id> and </sent_id>
        if inside_sent_id:
            columns = line.split('\t')  # Split line by tabs
            
            if len(columns) > 0 and '+' in columns[0]:  # Check if first column has '+'
                word = columns[0]
                if '_' in word:
                    # Split the word based on '+'
                    split_words = word.split('+')
                    
                    # Create new lines with split words
                    for split_word in split_words:
                        new_line = split_word + '\t' + '\t'.join(columns[1:])
                        output.append(new_line)
            else:
                output.append(line)
        else:
            output.append(line)

    # Write the output to a new file or print it
    with open("processed_output.txt", 'w', encoding='utf-8') as out_file:
        for line in output:
            out_file.write(line + '\n')

# Example usage
process_file('input/1')
