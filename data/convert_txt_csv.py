import os
import csv

# Directory containing the text files
input_directory = "/Users/user/Desktop/-explainable_recommender_systems/data/txtData"
# Directory where you want to save the CSV files
output_directory = "/Users/user/Desktop/-explainable_recommender_systems/data/csvData"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to convert a text file to CSV
def convert_text_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        # Read lines from the text file
        lines = txt_file.readlines()

    # Assuming the text file has a header row and data rows
    header = lines[0].strip().split('\t')  # Assuming tab-separated, modify as needed

    # Create a CSV writer
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header
        csv_writer.writerow(header)

        # Write the data rows
        for line in lines[1:]:
            data = line.strip().split('\t')  # Assuming tab-separated, modify as needed
            csv_writer.writerow(data)

# List all text files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):
        # Construct the full path to the input and output files
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(output_directory, filename.replace(".txt", ".csv"))

        # Convert the text file to CSV
        convert_text_to_csv(input_file, output_file)

print("Conversion completed.")
