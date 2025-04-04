import os
import csv

# Prompt user
root_dir = input("Enter the full path of the directory to scan: ").strip()

# Validate path
if not os.path.exists(root_dir):
    print(f"Error: Path '{root_dir}' does not exist.")
    exit(1)

output_file = "file_list.csv"
file_list = []

print(f"Scanning directory: {root_dir}...\n")

# Walk the directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        parent_folder = os.path.basename(dirpath)
        file_list.append([f"{parent_folder}/{filename}"])

if not file_list:
    print("No files found in the given directory.")
else:
    # Write results to CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(file_list)

    print(f"Success! Found {len(file_list)} files.")
    print(f"List saved to: {os.path.abspath(output_file)}")