
age = int(input("Enter your age: "))

match age:
    case 0:
        print("You are a baby.")
    case 1 | 2 | 3 | 4 | 5:
        print("You are a toddler.")
    case 6 | 7 | 8 | 9 | 10:
        print("You are a child.")
    case _ if age < 18:
        print("You are a teenager.")
    case _ if age >= 18 and age < 65:
        print("You are an adult.")
    case _ if age >= 65:
        print("You are a senior citizen.")
    case _:
        print("Invalid age entered.")