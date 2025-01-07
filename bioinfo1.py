# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from chembl_webresource_client.new_client import new_client

# Step 1: Target search for coronavirus
target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)

# Display all rows and columns for clarity
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print("Targets DataFrame:")
print(targets)

# Step 2: Select and retrieve bioactivity data for SARS coronavirus 3C-like proteinase (fifth entry)
selected_target = targets.target_chembl_id[4]  # Select fifth entry
print("Selected Target ChEMBL ID:", selected_target)

# Define bioactivity data
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
df = pd.DataFrame.from_dict(res)  # Convert to DataFrame
print("Bioactivity Data (First 3 rows):")
print(df.head(3))

# Verify the unique values in 'standard_type' column
print("Unique Standard Types:", df.standard_type.unique())

# Step 3: Data Cleaning (Convert 'value' to numeric and handle missing/invalid data)
if 'value' in df.columns:
    df['value'] = pd.to_numeric(df['value'], errors='coerce')  # Convert to numeric, set invalid to NaN
    df = df.dropna(subset=['value'])  # Remove rows with NaN values in 'value' column
    print(f"Number of valid IC50 entries: {len(df)}")

# Save bioactivity data to a CSV file
df.to_csv('bioactivity_data.csv', index=False)
print("Bioactivity data saved to 'bioactivity_data.csv'.")

# Step 4: Plotting IC50 Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['value'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of IC50 Values', fontsize=16)
plt.xlabel('IC50 (nM)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Step 5: Mount Google Drive to save the file
from google.colab import drive
drive.mount('/content/drive/', force_remount=True)

# Save the CSV file to Google Drive
df.to_csv('/content/drive/My Drive/bioactivity_data.csv', index=False)
print("Bioactivity data also saved to Google Drive.")

# Step 6: Iterate through 'molecule_chembl_id' to create a list
if 'molecule_chembl_id' in df.columns:
    mol_cid = []
    for i in df.molecule_chembl_id:
        mol_cid.append(i)

    # Print the first 5 molecule IDs to verify
    print("First 5 Molecule IDs:", mol_cid[:5])
else:
    print("Column 'molecule_chembl_id' not found in DataFrame.")

# Step 7: Fetch detailed information for the first 5 molecules
molecule = new_client.molecule
mol_details = []

for chembl_id in mol_cid[:5]:  # Example: Retrieve details for the first 5 molecules
    details = molecule.get(chembl_id)
    mol_details.append(details)

# Convert molecule details to DataFrame for easier visualization
mol_details_df = pd.DataFrame(mol_details)
print("Molecule Details DataFrame (First 5 rows):")
print(mol_details_df.head())

# Optional: Save molecule details to a CSV file
mol_details_df.to_csv('/content/drive/My Drive/molecule_details.csv', index=False)
print("Molecule details saved to 'molecule_details.csv' in Google Drive.")
