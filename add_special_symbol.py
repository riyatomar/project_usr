import re
import sys

# Function to generate a regular expression pattern for a word
def generate_pattern(word):
    return r"\b{}\b".format(re.escape(word))

# Function to perform replacements
def replace_strings(input_file_path, output_file_path):
    # Define the replacements
    sent_type = [
        "affirmative",
        "negative",
        "yn_interrogative",
        "interrogative",
        "imperative",
        "pass_affirmative",
        "pass_negative",
        "pass_interrogative",
        "pass_yn_interrogative",
        "fragment",
        "term",
        "title",
        "heading"
    ]
    
    const_list = [
        "span", "nil", "conj", "disjunct", "calender", "early_late", 
        "disjunction", "time_meas", "dist_meas", "mass_meas", "length_meas",
        "rate", "fraction", "compound"
    ]
    
    pronoun_list = ["wyax", "yax", "speaker", "addressee", "kim"]
    
    try:
        # Read the content of the input file
        with open(input_file_path, 'r') as file:
            content = file.read()
        
        # Perform replacements using regular expressions for const_list
        for old_str in const_list:
            if not old_str.startswith("_") and not old_str.startswith("-"):
                new_str = '*' + old_str
                pattern = generate_pattern(old_str)
                content = re.sub(pattern, new_str, content)
        
        # Perform replacements using regular expressions for pronoun_list
        for old_str in pronoun_list:
            if not old_str.startswith("_") and not old_str.startswith("-"):
                new_str = '$' + old_str
                pattern = generate_pattern(old_str)
                content = re.sub(pattern, new_str, content)
        
        # Perform replacements using regular expressions for sent_type
        for old_str in sent_type:
            if not old_str.startswith("_") and not old_str.startswith("-"):
                new_str = '%' + old_str
                pattern = generate_pattern(old_str)
                content = re.sub(pattern, new_str, content)
        
        # Write the modified content to the output file
        with open(output_file_path, 'w') as file:
            file.write(content)
        
        print("Replacements completed successfully. Output written to", output_file_path)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

# Check if the script is being run with the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python script.py input_file output_file")
else:
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    replace_strings(input_file_path, output_file_path)
