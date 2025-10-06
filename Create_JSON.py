import re, sys
import json

# Function to read the file and create JSON structure
def create_json_from_text(file_path):
    sentences = []
    project_id = "1"

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                parts = line.split('\t', 1)  # Split at the first tab
                if len(parts) == 2:
                    sentence_id, sentence = parts
                    sentences.append({
                        "project_id": project_id,
                        "sentence_id": sentence_id.strip(),
                        "sentence": sentence.strip()
                    })

    return {"sentences": sentences}

# Function to add spaces around special characters and clean sentence
def add_spaces_to_special_chars(sentence):
    # Handle hyphens: Add spaces around hyphens only if one side has a space
    sentence = re.sub(r"(?<!\S)-(?=\s)|(?<=\s)-(?=\S)|(?<=\S)-(?=\s)", r" - ", sentence)
    # Add spaces around other special characters
    sentence = re.sub(r"([!@#$%^&*()_=+\[\]{};:'\",<>/?`~।])", r" \1 ", sentence)
    # Replace multiple spaces with a single space
    sentence = re.sub(r"\s+", " ", sentence)
    return sentence.strip()

# File paths
input_text_file = sys.argv[1]
output_json_file = sys.argv[2]

# Step 1: Create JSON from text file
json_data = create_json_from_text(input_text_file)

# Step 2: Process sentences
for item in json_data["sentences"]:
    item["sentence"] = add_spaces_to_special_chars(item["sentence"])

# Step 3: Write final JSON
with open(output_json_file, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print(f"Processed JSON data has been written to {output_json_file}")
