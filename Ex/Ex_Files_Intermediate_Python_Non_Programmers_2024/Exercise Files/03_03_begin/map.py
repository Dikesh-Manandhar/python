class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]


# Challenge
# Use map to mulltiply all these numbers by 2

numbers = [1,2,3,4,5]

map_multiply= list(map(lambda number: number *2, numbers))

print(map_multiply)
