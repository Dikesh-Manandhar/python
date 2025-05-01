import sys
import os
script_name = os.path.basename(sys.argv[0])


todo=[]
# Read File
try:
    file = open("todo_data.txt", "r")
    todo = file.readlines()
    file.close()
except:
    pass


# Add Todo
if len(sys.argv)>=3 and sys.argv[1].lower() == "add":
    todo.append(f"{sys.argv[2]} \n")

# Remove Todo
if len(sys.argv)>=3 and sys.argv[1].lower() == "remove":
    try:
        todo.pop(int(sys.argv[2])-1)
    except Exception as e:
        print(e)
        sys.exit(1)


# Save File
file = open("todo_data.txt", "w")
file.writelines(todo)
file.close()

# Print List
if len(todo) == 0:
    print("Your ToDo list is empty :)")
else:
    print("\nHere's your ToDo list:\n")
    for x in range(len(todo)):
        print(f"{x+1}. {todo[x]}", end="")

print("\n*******************************\n")
print(f"To view ToDos:\n{script_name}")
print(f"\nTo add a ToDo:\n{script_name} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{script_name} remove 2\n")



