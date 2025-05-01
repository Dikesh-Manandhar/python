import pickle

# Pickle is a module that allows you to serialize and deserialize Python objects

age = 18

file = open("text.txt", "wb")  # Open a file in binary write mode
pickle.dump(age, file)  # Serialize the object and write it to the file
file.close()  # Close the file

file = open("text.txt", "rb")  # Open the file in binary read mode
age = pickle.load(file)  # Deserialize the object from the file
file.close()  # Close the file

print(age)  # Print the deserialized object
























class ToDo:
	def __init__(self, title, important, category = "Normal"):
		self.title = title
		self.important = important
		self.category = category


todos = [ToDo("Walk Dog", True), ToDo("Eat Cheese", False), ToDo("Learn Python", True, category = "Work")]
