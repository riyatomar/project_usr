import re
import sys

def extract_text_between_tags(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(r'<sent_id=(.*?)>', content)
            # print(matches)
            extracted_texts = [match[0:18] for match in matches]
            # print(extracted_texts)
            for text in extracted_texts:
                print(text)
            return extracted_texts, content

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def append_lines_to_extracted_texts(tsv_file_path, extracted_texts):
    try:
        with open(tsv_file_path, 'r', encoding='utf-8') as tsv_file:
            tsv_lines = tsv_file.readlines()

        new_content = ""
        for extracted_text in extracted_texts:
            for line in tsv_lines:
                if line.startswith(extracted_text):
                    new_content += line.strip() + '\n'
                    break

        return new_content

    except FileNotFoundError:
        print(f"File not found: {tsv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def insert_tsv_lines(text_content, matches, tsv_lines):
    for match, tsv_line in zip(matches, tsv_lines):
        pattern = f'<sent_id={match}[a-zA-Z]*>'
        text_content = re.sub(pattern, f'{tsv_line}\n<sent_id={match}>', text_content, count=1)
        # print(text_content)
    return text_content


if len(sys.argv) != 4:
    print("Usage: python script.py tsv_file_path text_file_path output_file_path")
else:
    tsv_file_path = sys.argv[1]
    text_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    extracted_texts, original_content = extract_text_between_tags(text_file_path)
    appended_content = append_lines_to_extracted_texts(tsv_file_path, extracted_texts)
    final_content = insert_tsv_lines(original_content, extracted_texts, appended_content.split('\n'))

    if final_content:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(final_content)

        print(f"Output saved to: {output_file_path}")
    else:
        print("Failed to generate output.")
