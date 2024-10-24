
import sys
import csv

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines

def read_tsv_file(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        tsv_data = [row for row in reader]
    return tsv_data

def match_lines(text_lines, tsv_data):
    matched_lines = []
    for text_line in text_lines:
        for tsv_line in tsv_data:
            if tsv_line[0] == text_line:
                matched_lines.append(tsv_line)
                break
    return matched_lines

def write_output_file(file_path, matched_lines):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(matched_lines)

def main(text_file_path, tsv_file_path, output_file_path):
    text_lines = read_text_file(text_file_path)
    tsv_data = read_tsv_file(tsv_file_path)
    matched_lines = match_lines(text_lines, tsv_data)
    write_output_file(output_file_path, matched_lines)
    print(f"Matched lines have been written to {output_file_path}")

# Example usage
text_file_path = sys.argv[1]
tsv_file_path = sys.argv[2]
output_file_path = 'output.tsv' 

main(text_file_path, tsv_file_path, output_file_path)

