import re
import sys
from collections import defaultdict

def extract_second_column_values(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into sentences
    sentences = re.split(r'(<Sentence id=\'.*?\'>)', content)

    # Initialize a dictionary to store the second column values for each sentence
    second_column_values = defaultdict(list)

    # Iterate through the sentences
    for i in range(1, len(sentences), 2):
        sentence_id = re.search(r'id=\'(\d+)\'', sentences[i]).group(1)
        sentence_content = sentences[i + 1]
        
        # Find all the words in the second column in the current sentence content
        values = re.findall(r'\d+\.\d+\t(\S+)\t', sentence_content)
        
        # Append the values to the list associated with the current sentence ID
        second_column_values[sentence_id].extend(values)

    return second_column_values

# Main script starts here
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file")
        sys.exit(1)
    
    filename = sys.argv[1]
    second_column_values = extract_second_column_values(filename)

    # Print the results
    for sentence_id, values in second_column_values.items():
        print(f"{' '.join(values)}")
