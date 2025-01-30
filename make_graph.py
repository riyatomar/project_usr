import matplotlib.pyplot as plt

# Data
construction_type = ['conj', 'cp', 'nc', 'ne', 'meas', 'disjunct', 'span', 'rate', 'spatial', 'calendar']
frequency = [1297, 1514, 712, 1137, 129, 216, 22, 5, 4, 0]

# Create bar graph
plt.figure(figsize=(10, 6))
plt.bar(construction_type, frequency, color='orange')

# Title and labels
plt.title('Frequency of Construction Types', fontsize=16)
plt.xlabel('Construction Type', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Display the plot
plt.show()
plt.savefig('output_graph.png')  # Save as a PNG file
