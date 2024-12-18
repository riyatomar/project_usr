import re

def extract_sent_ids(file_path):
    # Open the file and read the content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # List to store extracted sent_ids
    sent_ids = []

    # Regex to match <sent_id=some_id>
    sent_id_pattern = re.compile(r"<sent_id=([^\s>]+)>")

    # Iterate through each line in the file
    for line in content:
        match = sent_id_pattern.search(line)
        if match:
            sent_ids.append(match.group(1))

    return sent_ids


# File path to the file containing the data
file_path = 'usr_correction_id.txt'

# Extract sent_ids and print them
sent_ids = extract_sent_ids(file_path)
for sent_id in sent_ids:
    print(sent_id)
