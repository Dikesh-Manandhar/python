import random

class Animal:
    info="An animal is a living being"
    
    def __init__(self, name):
        print("An animal is created")
        self.name = name


class Dog(Animal):
    info="A dog is an animal"
    weight=20
    height=1

    def __init__(self, name, color):
        super().__init__(name)
        print("A dog is created")
        print("I'm big dog!")
        self.age = random.randint(1, 20)
        self.name = name
        self.color = color
    def bark(self):
        print(f"Woof! Woof! My name is {self.name}. My color is {self.color} and I'm {self.age} years old.")        

print(Dog.info)

dog1=Dog("Tommy", "black")

class Bulldog(Dog):

    def __init__(self, name, color):
        super().__init__(name, color)
        print("A bulldog is created")
        
dog1=Bulldog("Tommy", "black")

