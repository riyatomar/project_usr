import csv

def process_tsv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')
        rows = list(reader)

    processed_rows = []
    for row in rows:
        if len(row) >= 2 and row[0] == row[1]:
            row[0] = f"[{row[0]}]"
            row[1] = f"[{row[1]}]"
        processed_rows.append(row)
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerows(processed_rows)

# Example usage
input_file = 'sent.tsv'
output_file = 'sent_out.tsv'
process_tsv(input_file, output_file)
