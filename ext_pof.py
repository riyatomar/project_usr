# import re

# # Function to extract data containing 'pof__cn' and return the full block it belongs to
# def extract_pof_cn_data(input_file, output_file):
#     # Open the input file for reading
#     with open(input_file, 'r', encoding='utf-8') as file:
#         data = file.read()
    
#     # Split the data into blocks separated by <sent_id> tags
#     blocks = re.split(r'(<sent_id=[^>]+>)', data)
    
#     # Open the output file to write filtered blocks
#     with open(output_file, 'w', encoding='utf-8') as out_file:
#         for i in range(1, len(blocks), 2):
#             block_header = blocks[i]
#             block_body = blocks[i+1]
            
#             # Check if 'pof__cn' exists in the block body
#             if 'pof__cn' in block_body:
#                 out_file.write(block_header + block_body)

# # File paths
# input_file = '111stnd_final'  # Input file name
# output_file = 'pof_cn_filtered_data.txt'  # Output file name

# # Extract the blocks containing 'pof__cn'
# extract_pof_cn_data(input_file, output_file)

# print(f"Blocks with 'pof__cn' have been extracted to {output_file}.")


import re

# Function to extract data containing 'pof__cn' and remove them from the input file
def extract_and_remove_pof_cn_data(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()
    
    # Split the data into blocks separated by <sent_id> tags
    blocks = re.split(r'(<sent_id=[^>]+>)', data)
    
    # Lists to store blocks with and without 'pof__cn'
    blocks_with_pof_cn = []
    blocks_without_pof_cn = []
    custom_regex = r'-\t%[a-z]*\t-'
    # Iterate over blocks
    for i in range(1, len(blocks), 2):
        block_header = blocks[i]
        block_body = blocks[i + 1]
        
        # Check if 'pof__cn' exists in the block body
        if 'pof__cn' in block_body or 'nmod__adj' in block_body or 'lwg__vaux' in block_body or re.search(custom_regex, block_body):
            blocks_with_pof_cn.append(block_header + block_body)
        else:
            blocks_without_pof_cn.append(block_header + block_body)
    
    # Write blocks with 'pof__cn' to output file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write("".join(blocks_with_pof_cn))
    
    # Rewrite the input file with blocks without 'pof__cn'
    with open(input_file, 'w', encoding='utf-8') as in_file:
        in_file.write("".join(blocks_without_pof_cn))

# File paths
input_file = '11stnd_4ch-8ch'  # Input file name
output_file = 'pof_cn_filtered_data1.txt'  # Output file name

# Extract and remove blocks containing 'pof__cn'
extract_and_remove_pof_cn_data(input_file, output_file)

print(f"Blocks with 'pof__cn' have been extracted to {output_file} and removed from {input_file}.")
