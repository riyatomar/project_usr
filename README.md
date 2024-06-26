# Usage Instructions

## Adding Hindi Line
- Adds a Hindi line above each USR in a file from the corpus.
- Command:
    ```
    python3 add_hindi_line.py <tsv_file> <input_usr_file> <output_file>
    ```
    - `<tsv_file>`: Hindi corpus file with sentence ID separated by tabs.
    - `<input_usr_file>`: Text file containing USRs.
    - `<output_file>`: File to store the output.

## Adding Sent ID
- Adds `<sent_id>` tags in each USR.
- Command:
    ```
    python3 add_sent_id.py <input_usr_file> <output_file>
    ```
    - `<input_usr_file>`: Text file containing USRs.
    - `<output_file>`: File to store the output.

## Removing Sent ID
- Removes `<sent_id>` tags from each USR file within a folder
- Command:
    ```
    python3 remove_sent_id.py <input_usr_folder> 
    ```
    - `<input_usr_folder>`: Folder containing individual USR file 

## Adding Special Symbol
- Adds special symbols like "@", "%", "^" etc. in USRs.
- Command:
    ```
    python3 add_special_symbol.py <input_usr_file> <output_file>
    ```
    - `<input_usr_file>`: Text file containing USRs.
    - `<output_file>`: File to store the output.

## CSV USR Segregator
- Segregates the CSV format USRs into individual files with ID as their filename.
- Command:
    ```
    pyhton3 csv_usr_segregator.py <input_usr_file> <output_folder>
    ```
    - `<input_usr_file>`: Text file containing CSV format USRs.
    - `<output_folder>`: Folder to store the individual USR files after segregation.

## Vertical USR Segregator
- Segregates the vertical format USRs into individual files with ID as their filename.
- Command:
    ```
    pyhton3 csv_usr_segregator.py <input_usr_file> <output_folder>
    ```
    - `<input_usr_file>`: Text file containing vertical format USRs.
    - `<output_folder>`: Folder to store the individual USR files after segregation.

## Merger
- Merges the individual USR files into one compiled file.
- Command:
    ```
    python3 merger.py <input_folder> <output_file>
    ```
    - `<input_folder>`: Folder containing individual USR files.
    - `<output_file>`: Compiled USR output file.

## CSV to Vertical Format
- Converts CSV format USRs into Vertical Format USRs.
- Commands:
    ```
    python3 csv2vertical_format.py <input_folder> <output_folder>
    ```
    - `input_folder`: Folder containing CSV format USRs.
    - `output_folder`: Output Folder containing Vertical format USRs.

## Vertical to CSV Format
- Converts Vertical format USRs into CSV Format USRs.
- Commands:
    ```
    python3 vertical2csv_format.py <input_folder> <output_folder>
    ```
    - `input_folder`: Folder containing Vertical format USRs.
    - `output_folder`: Output Folder containing CSV format USRs.

## Vertical USR Format Checker
- Checks the format of Vertical USR 
- Command:
    ```
    python3 vertical_usr_format_checker.py <input_folder>
    ```
    - `<input_folder>`: Folder containing individual USR files.
    - Output will come in error_file.tsv

## Possible Concept Program
- Adds all the Possible Concepts from Dictionary just below each USR in the individual USR file
- Command:
    ```
    python3 possible_concept_program.py
    ```
