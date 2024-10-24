import sys

input_file_path = sys.argv[1] # USR mergerd file
output_file_path = sys.argv[2] # Output file after adding <sent_id>

keywords1 = [
    "%affirmative",
    "%negative",
    "%yn_interrogative",
    "%interrogative",
    "%imperative",
    "%pass_affirmative",
    "%pass_negative",
    "%pass_interrogative",
    "%pass_yn_interrogative",
    "%fragment",
    "%term",
    "%heading"
]

keywords2 = [
        "*span", "*nil", "*conj", "*disjunct", "*calender", "*early_late", 
        "*disjunction", "*time_meas", "*dist_meas", "*mass_meas", "*length_meas",
        "*rate", "*fraction", "*compound"
    ]
# keywords1 = [keyword.lower() for keyword in keywords1]
# keywords2 = [keyword.lower() for keyword in keywords2]

keyword1_found = False

with open(input_file_path, 'r', encoding="utf-8") as input_file, open(output_file_path, 'w', encoding="utf-8") as output_file:
    for line in input_file:
        if line.startswith("Geo_") and "coref" not in line:
            line = "<sent_id=" + line.rstrip() + ">\n"
        # Check if any keyword from keywords1 is present in the line
        if any(keyword in line for keyword in keywords1):
            keyword1_found = True
            output_file.write(line)
        elif keyword1_found:
            keyword1_found = False
            if any(keyword in line for keyword in keywords2):
                # If the next line contains any keyword from keywords2, add "</sent_id>"
                output_file.write(line + "</sent_id>\n")
            else:
                # If the next line is empty, add "nil" to that line
                if not line.strip():
                    output_file.write("")
                output_file.write("</sent_id>\n" + line)
        else:
            output_file.write(line) # Write the line to the output file

print("--------------------")
print("sent_id added to USRs.")
