
file_path = 'format_error.tsv'

# Create a set to store unique first column values
unique_first_column = set()

# Open and read the file
with open(file_path, 'r') as file:
    for line in file:
        # Split the line by spaces or tabs and take the first column value
        first_column_value = line.split()[0]
        # Add the value to the set (sets automatically handle uniqueness)
        unique_first_column.add(first_column_value)

# Convert the set to a sorted list for display
unique_values_list = sorted(unique_first_column)

# Print the unique values
print("Unique values in the first column:")
for value in unique_values_list:
    print(value)
