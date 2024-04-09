# Add Hindi Line
- This is to add the Hindi line above each USR in a file from the corpus
- Command to run:
    python3 add_hindi_line.py <tsv_file> <input_usr_file> <output_file>
        - tsv_file: Hindi corpus file with sentence ID separated by tabs
        - input_usr_file: Text file conatining USRs
        - output_file: File to store the Output

# Add Sent ID
- This is to add <sent_id> tags in each USR
- Command to run:
    python3 add_sent_id.py <input_usr_file> <output_file>
        - input_usr_file: Text file conatining USRs
        - output_file: File to store the Output

# Add Special Symbol
- This is to add special symbols like "@", "%", "^" etc in USR 
- Command to run:
    python3 add_special_symbol.py <input_usr_file> <output_file>
        - input_usr_file: Text file conatining USRs
        - output_file: File to store the Output

# CSV USR Segregator
- This is to segregate the csv format USRs into individual files with ID as their filename
- Command to run:
    pyhton3 csv_usr_segregator.py <input_usr_file> <output_folder>
        - input_usr_file: Text file conatining csv format USRs
        - output_folder: folder to store the individual USR files after segregation

# Vertical USR Segregator
- This is to segregate the vertical format USRs into individual files with ID as their filename
- Command to run:
    pyhton3 csv_usr_segregator.py <input_usr_file> <output_folder>
        - input_usr_file: Text file conatining vertical format USRs
        - output_folder: folder to store the individual USR files after segregation

# Merger
- Merger is to merge the individual USR files into one compiled file
- Command to run merger:
    python3 merger.py <input_folder> <output_file>
        - input_folder: folder containing USR files
        - output_file: COmpiled USR output file

#


