import os
import re

class SentenceIndexChecker:
    def __init__(self, file_path):  # Corrected __init__ method
        self.file_path = file_path
        self.current_sentence_id = None

    def check_index(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()

                if line.startswith("<sent_id="):
                    self.current_sentence_id = self.extract_sentence_id(line)
                elif line.startswith("#") or line.startswith("%") or line.startswith("</sent_id>") or line.startswith("pass"):
                    continue  # Skip metadata and sentence end tags
                elif line:
                    self.process_token_line(line)

    def extract_sentence_id(self, line):
        return line.split('=')[1].strip('>').replace('\t', ' ')

    def process_token_line(self, line):
        token_info = re.split(r'\s+', line)
        
        # Check if the second column is missing or invalid (empty or not an integer)
        if len(token_info) > 1:
            second_column = token_info[1]
            if not second_column.isdigit():
                print(f"File: {self.file_path}, Sentence ID: {self.current_sentence_id}, Invalid second column: {line}")

def process_all_files_in_folder(input_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_folder, filename)
            checker = SentenceIndexChecker(input_file_path)
            checker.check_index()

# Define input folder
input_folder = '/home/riya/project_usr/check5k'  # Replace with your folder path

# Process all files in the folder
process_all_files_in_folder(input_folder)
