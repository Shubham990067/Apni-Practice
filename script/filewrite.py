shubham="command"
class_code = f'''
class MyClass({shubham}):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,!".format(self.name))


my_object = MyClass("John")
my_object.greet()
'''

# Specify the file path and name
file_path = "C:/Users/158202/Downloads/ZCORETestFramework/ZCORETestFramework/output.py"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the class code into the file
    file.write(class_code)

print("File created successfully!")
