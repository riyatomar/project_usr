def sort_sentences(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()
    
    # Split the data by entries
    entries = data.strip().split('\n\n')

    # Create a list to hold tuples of (sent_id, entry)
    sorted_entries = []

    for entry in entries:
        # Check if the entry has a sent_id
        if '<sent_id=' in entry:
            sent_id_start = entry.find('<sent_id=') + len('<sent_id=')
            sent_id_end = entry.find('>', sent_id_start)
            sent_id = entry[sent_id_start:sent_id_end]
            sorted_entries.append((sent_id, entry))
    
    # Sort the entries by the sent_id
    sorted_entries.sort(key=lambda x: x[0])

    # Prepare the output data
    output_data = '\n\n\n'.join(entry[1] for entry in sorted_entries)

    # Write the sorted data to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_data)

# Define input and output file paths
input_file = 'output_file.txt'  # Replace with your input file path
output_file = 'output_order.txt'  # Replace with your desired output file path

# Call the function to sort and write the sentences
sort_sentences(input_file, output_file)
