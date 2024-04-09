'''
This code will calculate the frequency all the dependency and 
discourse relations in 6th and 7th row respectively.

Command to run this code: python data_observation.py filename
    >>>filename is the file containing number of enclosed USRs.
    >>>Output will be stored into "output.tsv" file
    
'''

import sys
import re
import csv
from collections import Counter

usr_file = sys.argv[1] #input file
output_file = "output.tsv" #output file

with open(usr_file, "r", encoding="utf-8") as uf:
    lines = uf.readlines()
   
    extracted_text = []

    for line in lines:
        if line.startswith('<sent_id'):
            # Find line index for the current line
            line_index = lines.index(line)
            
            if line_index + 6 < len(lines):
                line6 = lines[line_index + 6]
                matches = re.findall(r':(.*?)(,|\n)', line6)
                extracted_text.extend(match[0] for match in matches)

            if line_index + 7 < len(lines):
                line7 = lines[line_index + 7]
                matches = re.findall(r':(.*?)(,|\n)', line7)
                extracted_text.extend(match[0] for match in matches)

    # Count the frequency of each relation in 6th and 7th row
    frequency_counter = Counter(extracted_text)
    # print(extracted_text)

with open(output_file, 'w', newline='') as tsvfile:
    csvwriter = csv.writer(tsvfile, delimiter='\t')
    csvwriter.writerow(["Relation", "Frequency"])  # Header row
    for text, count in frequency_counter.items():
        csvwriter.writerow([text, count])

print(f"Output saved to {output_file}")
