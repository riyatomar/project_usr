import os
from docx import Document

def docx_to_txt(docx_file, output_folder):
    # Open the .docx file
    document = Document(docx_file)
    # Extract the filename without the extension
    filename = os.path.basename(docx_file).replace('.docx', '.txt')
    # Create a .txt file path in the output folder
    txt_file_path = os.path.join(output_folder, filename)
    
    # Open the .txt file for writing
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        # Loop through the paragraphs in the document and write to the .txt file
        for paragraph in document.paragraphs:
            txt_file.write(paragraph.text + '\n')  # Write each paragraph and add a newline

    print(f"Converted {docx_file} to {txt_file_path}")

def convert_folder_of_docx(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.docx'):
            docx_file = os.path.join(input_folder, filename)
            docx_to_txt(docx_file, output_folder)

# Set the paths
input_folder = '/home/lc4eu/LC/project_usr/usg_workshop_5k_complete_new_cnx_usr'
output_folder = '5k_data'  # Replace with the folder where you want to save .txt files

# Convert all .docx files in the input folder to .txt
convert_folder_of_docx(input_folder, output_folder)