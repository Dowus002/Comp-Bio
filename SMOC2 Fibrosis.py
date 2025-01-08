import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# Adjust display options to show all rows and columns
pd.set_option('display.max_rows', None)       # Show all rows
pd.set_option('display.max_columns', None)    # Show all columns
pd.set_option('display.max_colwidth', None)   # Remove column width limit
pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping to multiple lines

# Update the file path to where the 'fibrosis_smoc2_rawcounts.csv' file is located on your system
file_path = '/Users/darrylowusuansah/Downloads/fibrosis_smoc2_rawcounts.csv'  

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first 5 rows of the dataset to ensure it's loaded correctly
print(df.head(45))

# Check the column names to ensure we're referencing the correct one
print("Column Names:", df.columns)

# Filter the data to remove rows where any value in the row is 0
filtered_data = df[(df != 0).all(axis=1)]  # This checks if all values in the row are non-zero
print("Filtered Data:")
print(filtered_data.head(45))  # Show the filtered data

# Save the filtered data to a new CSV file for later use   
filtered_data.to_csv('/Users/darrylowusuansah/Downloads/filtered_data_smoc2.csv', index=False)
print("\nFiltered data saved to 'filtered_data_smoc2.csv'.")

# Now we will create the four plots as requested

# Plot 1: Normal vs Fibrosis (1)
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_fibrosis1'], filtered_data['smoc2_normal1'], color='blue', alpha=0.6)
plt.title('Comparison: smoc2_fibrosis1 vs smoc2_normal1')
plt.xlabel('smoc2_fibrosis1 (Fibrosis)')
plt.ylabel('smoc2_normal1 (Normal)')
plt.plot([min(filtered_data['smoc2_fibrosis1']), max(filtered_data['smoc2_fibrosis1'])],
         [min(filtered_data['smoc2_fibrosis1']), max(filtered_data['smoc2_fibrosis1'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_fibrosis1'].iloc[i], 
             filtered_data['smoc2_normal1'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.show()

# Plot 2: Normal Attenuated vs Fibrosis Attenuated
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_fibrosis2'], filtered_data['smoc2_normal4'], color='green', alpha=0.6)
plt.title('Comparison: smoc2_fibrosis2 vs smoc2_normal4 (Attenuated)')
plt.xlabel('smoc2_fibrosis2 (Fibrosis Attenuated)')
plt.ylabel('smoc2_normal4 (Normal Attenuated)')
plt.plot([min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         [min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_fibrosis2'].iloc[i], 
             filtered_data['smoc2_normal4'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.show()

# Plot 3: Fibrosis (1) vs Fibrosis Attenuated
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_fibrosis2'], filtered_data['smoc2_fibrosis1'], color='orange', alpha=0.6)
plt.title('Comparison: smoc2_fibrosis2 vs smoc2_fibrosis1')
plt.xlabel('smoc2_fibrosis2 (Fibrosis Attenuated)')
plt.ylabel('smoc2_fibrosis1 (Fibrosis)')
plt.plot([min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         [min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_fibrosis2'].iloc[i], 
             filtered_data['smoc2_fibrosis1'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.show()

# Plot 4: Normal vs Normal Attenuated
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_normal4'], filtered_data['smoc2_normal1'], color='purple', alpha=0.6)
plt.title('Comparison: smoc2_normal4 vs smoc2_normal1')
plt.xlabel('smoc2_normal4 (Normal Attenuated)')
plt.ylabel('smoc2_normal1 (Normal)')
plt.plot([min(filtered_data['smoc2_normal4']), max(filtered_data['smoc2_normal4'])],
         [min(filtered_data['smoc2_normal4']), max(filtered_data['smoc2_normal4'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_normal4'].iloc[i], 
             filtered_data['smoc2_normal1'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.show()

# Optional: Save each plot as an image
# Save Plot 1
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_fibrosis1'], filtered_data['smoc2_normal1'], color='blue', alpha=0.6)
plt.title('Comparison: smoc2_fibrosis1 vs smoc2_normal1')
plt.xlabel('smoc2_fibrosis1 (Fibrosis)')
plt.ylabel('smoc2_normal1 (Normal)')
plt.plot([min(filtered_data['smoc2_fibrosis1']), max(filtered_data['smoc2_fibrosis1'])],
         [min(filtered_data['smoc2_fibrosis1']), max(filtered_data['smoc2_fibrosis1'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_fibrosis1'].iloc[i], 
             filtered_data['smoc2_normal1'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.savefig('/Users/darrylowusuansah/Downloads/compare_normal_fibrosis.png', dpi=300)

# Save Plot 2
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_fibrosis2'], filtered_data['smoc2_normal4'], color='green', alpha=0.6)
plt.title('Comparison: smoc2_fibrosis2 vs smoc2_normal4 (Attenuated)')
plt.xlabel('smoc2_fibrosis2 (Fibrosis Attenuated)')
plt.ylabel('smoc2_normal4 (Normal Attenuated)')
plt.plot([min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         [min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_fibrosis2'].iloc[i], 
             filtered_data['smoc2_normal4'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.savefig('/Users/darrylowusuansah/Downloads/compare_fibrosis_normal_attenuated.png', dpi=300)

# Save Plot 3
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_fibrosis2'], filtered_data['smoc2_fibrosis1'], color='orange', alpha=0.6)
plt.title('Comparison: smoc2_fibrosis2 vs smoc2_fibrosis1')
plt.xlabel('smoc2_fibrosis2 (Fibrosis Attenuated)')
plt.ylabel('smoc2_fibrosis1 (Fibrosis)')
plt.plot([min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         [min(filtered_data['smoc2_fibrosis2']), max(filtered_data['smoc2_fibrosis2'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_fibrosis2'].iloc[i], 
             filtered_data['smoc2_fibrosis1'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.savefig('/Users/darrylowusuansah/Downloads/compare_fibrosis_vs_fibrosis_attenuated.png', dpi=300)

# Save Plot 4
plt.figure(figsize=(12, 8))
plt.scatter(filtered_data['smoc2_normal4'], filtered_data['smoc2_normal1'], color='purple', alpha=0.6)
plt.title('Comparison: smoc2_normal4 vs smoc2_normal1')
plt.xlabel('smoc2_normal4 (Normal Attenuated)')
plt.ylabel('smoc2_normal1 (Normal)')
plt.plot([min(filtered_data['smoc2_normal4']), max(filtered_data['smoc2_normal4'])],
         [min(filtered_data['smoc2_normal4']), max(filtered_data['smoc2_normal4'])],
         color='red', linestyle='--')
for i, ensembl_id in enumerate(filtered_data['Unnamed: 0']):
    plt.text(filtered_data['smoc2_normal4'].iloc[i], 
             filtered_data['smoc2_normal1'].iloc[i], 
             ensembl_id, fontsize=8, alpha=0.7)
plt.grid(True)
plt.savefig('/Users/darrylowusuansah/Downloads/compare_normal_vs_normal_attenuated.png', dpi=300)

print("\nAll plots saved as images.")
