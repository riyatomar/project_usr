import os

def search_files_for_keywords(folder_path, keywords):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for file_name in files:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Check if any of the keywords are in the file content
                if any(keyword.lower() in content.lower() for keyword in keywords):
                    print(f"{file_name}")
                    
        except Exception as e:
            print(f"Could not read file {file_name}: {e}")

# Folder path containing the files
folder_path = '/home/riya/project_usr/vertical_segregated_5k_USRs/'

# keywords = ['rate', 'calendar', 'calender', 'Rate', 'Calendar', 'Calender']
# keywords = ['meas', 'Meas']
keywords = ['yA_huA_hE', 'yA_huA_WA']
# Run the search function
search_files_for_keywords(folder_path, keywords)
