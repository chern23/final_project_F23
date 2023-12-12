import csv

# Open the original CSV file for reading
with open('final_project_F23/NGA/NGA_QID_export.csv', 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Choose the column index you want to extract (replace 1 with the desired index)
    column_index = 12

    # Extract values from the chosen column
    column_values = [row[column_index] for row in csv_reader]

# Open a new CSV file for writing
with open('wikidataid_artworks.csv', 'w', newline='', encoding='utf-8') as output_file:
    # Create a CSV writer
    csv_writer = csv.writer(output_file)

    # Write the column values to the new CSV file
    csv_writer.writerow(column_values)

print(f"Values from column {column_index} written to output_file.csv")
