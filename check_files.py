import os
import csv

# Input file paths
subpaths_file = "file_list.csv"       # The CSV with subpaths (from your earlier script)
fullpaths_file = "full_paths.csv"     # The CSV with full paths
output_file = "not_found_subpaths.csv"

# Load subpaths
with open(subpaths_file, newline='') as f:
    reader = csv.reader(f)
    subpaths = [row[0] for row in reader if row]  # Skip empty rows

# Remove header if present
if subpaths[0].lower() == "subpath":
    subpaths = subpaths[1:]

# Load full paths
with open(fullpaths_file, newline='') as f:
    reader = csv.reader(f)
    fullpaths = [row[0] for row in reader if row]

# Find subpaths not present in full paths
not_found = []
for sub in subpaths:
    found = any(sub in full for full in fullpaths)
    if not found:
        not_found.append([sub])

# Write result
with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Subpath"])
    writer.writerows(not_found)

print(f"Done! {len(not_found)} subpaths not found.")
print(f"Saved to: {os.path.abspath(output_file)}")