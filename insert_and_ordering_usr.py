# Define file paths
geo_file_path = 'geo_file.txt'  # Path to the first file
second_file_path = 'second_file.txt'  # Path to the second file
final_output_file_path = 'output_order.txt'  # Path to the final output file

# Function to read the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Function to sort sentences by sent_id
def sort_sentences(merged_sentences, output_file):
    # Prepare the merged data as a single string
    data = ''.join(merged_sentences)
    
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
    output_data = '\n\n\n\n'.join(entry[1] for entry in sorted_entries)

    # Write the sorted data to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_data)

# Read contents of both files
geo_sentences = read_file(geo_file_path)
second_sentences = read_file(second_file_path)

# Prepare to merge sentences
merged_sentences = []

# Add geo sentences
merged_sentences.extend(geo_sentences)

# Add second file sentences
merged_sentences.extend(second_sentences)

print("Merging complete! Proceeding to sort the merged content.")

# Call the function to sort and write the sentences
sort_sentences(merged_sentences, final_output_file_path)

print("Sorting complete! Check the final output file.")
