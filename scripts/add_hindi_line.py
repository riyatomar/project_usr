import sys
import re

epcf = open(sys.argv[1], 'r', encoding='utf-8')  # Read the Hindi corpora file
epcfr = epcf.readlines()
PCdict = {}
for i in range(len(epcfr)):
    if len(epcfr[i].split()) > 2:
        PCdict[epcfr[i].split('\t')[0]] = epcfr[i].split('\t')[1]

usrf = open(sys.argv[2], 'r', encoding='utf-8')  # Read the USR file
usrfr = usrf.readlines()
usr_text = ''.join(usrfr)

# Extract partial matches of <sent_id> tags
matches = re.findall(r'<sent_id=(.*?)>', usr_text)
extracted_ids = [match[0:17] for match in matches]

# Keep track of processed IDs
processed_ids = set()

# Function to perform partial matching
def partial_match(s, substr):
    index = s.find(substr)
    return index if index != -1 else len(s)

# Perform partial matching and add corresponding extracted_ids above their matches
for text in extracted_ids:
    # Modify the regular expression to allow for additional characters after {text}
    pattern = re.escape(f"<sent_id={text}")
    match = re.search(pattern, usr_text)
    
    if match:
        start_index = match.start()
        end_index = match.end()
        usr_text = usr_text[:start_index] + f"#{text}: {PCdict.get(text, 'UNKNOWN')}" + f"<sent_id= {text}" + usr_text[end_index:]
        processed_ids.add(text)


output_file_path = 'output.txt'  
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(usr_text)

print(f"Modified content written to {output_file_path}")
