file = open("numbers.txt","r")
lines=file.readlines()

#Multiply all the numbers in the file by 2
for line in range(len(lines)):
        lines[line] = str(float(lines[line]) * 2) + "\n"
    


file = open("numbers.txt","w")
lines = file.writelines(lines)
file.close()