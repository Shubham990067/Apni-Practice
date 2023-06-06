import csv


def write_data_to_file(csv_file, output_file):
    # Open the CSV file for reading
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        # Open the output file for writing
        with open(output_file, 'w') as output:
            writer = csv.writer(output)

            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Write the row to the output file
                writer.writerow(row)

    print("Data has been written to", output_file)


# Specify the path to the CSV file and the output file
csv_file_path = 'C:/Users/158202/Downloads/ZCORETestFramework/ZCORETestFramework/out/data.csv'
output_file_path = 'C:/Users/158202/Downloads/ZCORETestFramework/ZCORETestFramework/output.py'

# Call the function to write data to the file
write_data_to_file(csv_file_path, output_file_path)
