def check_sent_id_pairs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    open_tags = []
    mismatched_closures = []
    mismatched_openings = []

    for line_num, line in enumerate(lines, 1):
        if '<sent_id=' in line:
            # Extract the tag and track it
            start_index = line.find('<sent_id=')
            end_index = line.find('>', start_index) + 1
            tag = line[start_index:end_index].strip()
            open_tags.append((tag, line_num))

        if '</sent_id>' in line:
            if open_tags:
                # Match the last opened tag
                open_tags.pop()
            else:
                # Closing tag without opening
                mismatched_closures.append((line.strip(), line_num))

    # Remaining open tags are unmatched
    mismatched_openings.extend(open_tags)

    # Report results
    print("Mismatched tags summary:\n")

    if mismatched_openings:
        print("Unmatched <sent_id= tags:")
        for tag, line_num in mismatched_openings:
            print(f"  Line {line_num}: {tag}")
    else:
        print("No unmatched <sent_id= tags.")

    if mismatched_closures:
        print("\nUnmatched </sent_id> tags:")
        for tag, line_num in mismatched_closures:
            print(f"  Line {line_num}: {tag}")
    else:
        print("\nNo unmatched </sent_id> tags.")

# Usage
file_path = '/home/lc4eu/LC/project_usr/5k_data/nios_1ch_new_cnx.txt'  # Replace with your actual file path
check_sent_id_pairs(file_path)
