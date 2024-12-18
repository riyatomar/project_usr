def process_input_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []

    for line in lines:
        if '+' in line:
            parts = line.split('+')
            # print(parts)
            second_part = parts[1].strip()
            if '-' in second_part:
                print(second_part)
                # # Split at '-' and move content after '+' to the next line
                # hyphen_index = second_part.index('-')
                # line = second_part[:hyphen_index] + '\n'
                # processed_lines.append(line)
                # processed_lines.append(parts[1].strip() + '\n')
                if second_part.count('-') > 1:

                    hyphen_index = second_part.index('-')
                    # print(hyphen_index)
                    line = second_part[hyphen_index:0] + '\n'
                    print(second_part[hyphen_index:0])
                    processed_lines.append(line)
                    processed_lines.append(parts[1].strip() + '\n')
                else:
                    processed_lines.append(line)

            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)

    return processed_lines

# Example usage:
input_file = '/home/riya/codes/data/test'  # Replace with your actual input file path
processed_lines = process_input_file(input_file)

# # Print the processed output
# for line in processed_lines:
#     print(line.strip())
