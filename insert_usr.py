# Define file paths
geo_file_path = '12_pof_cn_filtered_data.txt'  # Path to the first file
second_file_path = '12_pof_cn_filtered_data1.txt'  # Path to the second file
output_file_path = 'output_file.txt'  # Path to the output file

# Function to read the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Read contents of both files
geo_sentences = read_file(geo_file_path)
second_sentences = read_file(second_file_path)

# Prepare to merge sentences
merged_sentences = []

# Add geo sentences
merged_sentences.extend(geo_sentences)

# Add second file sentences
merged_sentences.extend(second_sentences)

# Join the merged sentences and write to output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(merged_sentences)

print("Merging complete! Check the output file.")


