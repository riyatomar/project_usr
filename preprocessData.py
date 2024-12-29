import re
import json

# Read input data from a file
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Write output data to a file
def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Function to add spaces around special characters and remove multiple spaces
# def add_spaces_to_special_chars(sentence):
#     # Add spaces around special characters
#     sentence = re.sub(r"([!@#$%^&*()\-_=+\[\]{};:'\",<>./?`~।])", r" \1 ", sentence)
#     # Replace multiple spaces with a single space
#     sentence = re.sub(r"\s+", " ", sentence)
#     return sentence.strip()

def add_spaces_to_special_chars(sentence):
    # Handle hyphens: Add spaces around hyphens only if one side has a space
    sentence = re.sub(r"(?<!\S)-(?=\s)|(?<=\s)-(?=\S)|(?<=\S)-(?=\s)", r" - ", sentence)
    # Add spaces around other special characters
    sentence = re.sub(r"([!@#$%^&*()_=+\[\]{};:'\",<>/?`~।])", r" \1 ", sentence)
    # Replace multiple spaces with a single space
    sentence = re.sub(r"\s+", " ", sentence)
    return sentence.strip()

input_file = 'input.json'
output_file = 'output.json'

data = read_json_file(input_file)
for item in data["sentences"]:
    item["sentence"] = add_spaces_to_special_chars(item["sentence"])

# Write the modified data back to a file
write_json_file(output_file, data)
