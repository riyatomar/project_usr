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

# File path of the input text file
input_file = "segments.txt"

# Create JSON data
json_data = create_json_from_text(input_file)

# Output JSON to a file or print it
output_file = "input.json"
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print(f"JSON data has been written to {output_file}")
