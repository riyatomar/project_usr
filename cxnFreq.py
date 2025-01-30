# import re
# from collections import Counter

# # Predefined lists of special strings
# nc_list = [
#     "3-waw", "4-waw", "5-waw", "6-waw", "7-waw", "naF-waw", "2-waw", 
#     "karmaXAraya", "xvigu", "2-bahubrIhi", "3-bahubrIhi", "4-bahubrIhi", 
#     "5-bahubrIhi", "6-bahubrIhi", "7-bahubrIhi", "xvanxva", "nc",
#     "avyayIBAva", "upapaxa", "maXyamapaxalopI", "compound"
# ]

# meas_list = ['time_meas', 'dist_meas', 'length_meas', 'width_meas', 'temp_meas',
#             'depth_meas', 'height_meas', 'volume_meas', 'weight_meas']

# def count_grouped_bracketed_strings(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         text = file.read()
    
#     # Find all occurrences of strings within square brackets
#     bracketed_strings = re.findall(r'\[(.*?)\]', text)
    
#     # Filter out entries that contain "shade"
#     filtered_strings = [s for s in bracketed_strings if "shade" not in s]
    
#     # Extract prefixes (everything before the underscore) if applicable
#     grouped_strings = [re.split(r'_\d+', string)[0] for string in filtered_strings]
    
#     # Initialize a counter for frequencies
#     frequency_count = Counter()
    
#     for string in grouped_strings:
#         if string in nc_list:
#             frequency_count['nc'] += 1  # Add to 'nc' if in nc_list
#         elif string in meas_list:
#             frequency_count['meas'] += 1  # Add to 'meas' if in meas_list
#         else:
#             frequency_count[string] += 1  # Add the string as is if neither
    
#     # Print the frequencies
#     for string, count in frequency_count.items():
#         print(f'{string}: {count}')

# # Example usage
# filename = 'second_file.txt'  # Change this to the actual filename
# count_grouped_bracketed_strings(filename)



import re
import os
from collections import Counter

# Predefined lists of special strings
nc_list = [
    "3-waw", "4-waw", "5-waw", "6-waw", "7-waw", "naF-waw", "2-waw",
    "karmaXAraya", "xvigu", "2-bahubrIhi", "3-bahubrIhi", "4-bahubrIhi", 
    "5-bahubrIhi", "6-bahubrIhi", "7-bahubrIhi", "xvanxva", "nc",
    "avyayIBAva", "upapaxa", "maXyamapaxalopI", "compound",
    "compound_ 1", "6-wawa", "xvanda", "waw", "6-waw-1", "7-bahuvrIhi", "[6-waw",
    "xvanxva_", "bahuvrIhi", "xvanxa", "6-bahivrIhi", "6-bahuvrIhi", "waxXiwa", "maXyamalopI", "maXymalopI1",
]

meas_list = ['time_meas', 'dist_meas', 'length_meas', 'width_meas', 'temp_meas',
            'depth_meas', 'height_meas', 'volume_meas', 'weight_meas', 'degree_meas', 'mass_meas', 'speed_meas',
            ]

def count_grouped_bracketed_strings_in_folder(folder_path):
    # Initialize a counter for frequencies
    frequency_count = Counter()

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Only process files (not directories)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            # Find all occurrences of strings within square brackets
            bracketed_strings = re.findall(r'\[(.*?)\]', text)
            
            # Filter out entries that contain "shade"
            filtered_strings = [s for s in bracketed_strings if "shade" not in s]
            
            # Extract prefixes (everything before the underscore) if applicable
            grouped_strings = [re.split(r'_\d+', string)[0] for string in filtered_strings]
            
            # Count the occurrences of strings
            for string in grouped_strings:
                if string in nc_list:
                    frequency_count['nc'] += 1  # Add to 'nc' if in nc_list
                elif string in meas_list:
                    frequency_count['meas'] += 1  # Add to 'meas' if in meas_list
                else:
                    frequency_count[string] += 1  # Add the string as is if neither
    
    # Print the frequencies
    for string, count in frequency_count.items():
        print(f'{string}: {count}')

# Example usage
folder_path = '5k_data'
count_grouped_bracketed_strings_in_folder(folder_path)
