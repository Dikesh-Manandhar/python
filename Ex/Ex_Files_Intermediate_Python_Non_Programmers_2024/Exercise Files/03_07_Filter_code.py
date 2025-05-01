# Use print("messages...") to debug your solution.

class Student:
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def __repr__(self): 
		return f"{self.name}: {self.score}"
	
students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63), Student("Mary", 0.55)]



def m_students():
	return list(filter(lambda student: student.name[0] == "M", students))