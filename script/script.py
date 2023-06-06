import csv

#
# class Person:
#     def __init__(self, id, name, age, gender):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def __str__(self):
#         return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
#
#
# def generate_persons_from_csv(csv_file):
#     persons = []
#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             person = Person(row['id'], row['name'], row['age'], row['gender'])
#             persons.append(person)
#     return persons
#
#
# # Usage example
# csv_file = 'out/data.csv'
# persons = generate_persons_from_csv(csv_file)
#
# for person in persons:
#     print(person)
import csv

class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Hobbies: {', '.join(self.hobbies)}"

def generate_persons_from_csv(csv_file):
    persons = []
    client=[]
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name = row[0]
            age = int(row[1])
            hobbies = row[2:]
            person = Person(name, age, hobbies)
            persons.append(person)
            client.append(person)

    return persons,client

# Usage example
csv_file = 'out/data1.csv'
persons,client = generate_persons_from_csv(csv_file)

for person in persons:
    print(person)

for person in client:
    print(person)
