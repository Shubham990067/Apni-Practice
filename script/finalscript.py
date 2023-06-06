import csv


# Function to create a Python file and write classes into it
def create_python_file(classes):
    file_name = "classes.py"
    with open(file_name, 'w') as file:
        for class_name, parameters in classes.items():
            file.write(f"\nclass {class_name}:\n")
            file.write(f"    def __init__(self, {', '.join(parameters)}):\n")
            for param in parameters:
                file.write(f"\n        self.{param} = {param}")
            for param in parameters:
                print(f'    super().__init__(self.'{.join(parameters)}')')



# Read the CSV file and extract class names and parameters
def read_csv_file(file_name):
    classes = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
            if len(row) >= 2:  # Check if the row has at least two columns
                class_name = row[0]
                parameters = row[1:]
                classes[class_name] = parameters
            else:
                print(f"Skipping invalid row: {row}")
    return classes


# Example usage
csv_file_name = "C:/Users/158202/Downloads/ZCORETestFramework/ZCORETestFramework/out/data.csv"
class_data = read_csv_file(csv_file_name)
create_python_file(class_data)
