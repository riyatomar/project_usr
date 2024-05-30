import re
import sys
# Read input text
with open(sys.argv[1], "r", encoding="utf-8") as file:
    input_text = file.read()

# Define regex pattern
pattern = r'<sent_id=(.*?)</sent_id>'

# Find matches
matches = re.findall(pattern, input_text, re.DOTALL)

# Filter matches
filtered_matches = []
for match in matches:
    if "nil" not in match:
        filtered_matches.append(match.strip())

# Print filtered matches
for match in filtered_matches:
    print(match)
