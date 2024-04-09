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
    - `<input_folder>`: Folder containing USR files.
    - `<output_file>`: Compiled USR output file.

