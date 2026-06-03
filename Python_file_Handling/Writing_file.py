# writing files
file11 = open("fileDemo2.txt", "w")
file11.write("This is the third line of the file.\n")
file11.write("This is the fourth line of the file.\n")
file11.close()

# write a program to write multiple line to a text file using writelines() method
file12 = open("C:\\Users\\Niyati\\VS python tutorials\\fileDemo2.txt", "w")
lines12 = [
    "This is a python program.\n",
    "python is superb.\n",
    "This is powerful programming language.\n",
]
file12.writelines(lines12)
file12.close()

# write a program to append a line to the existing file
file13 = open("fileDemo2.txt", "a")
file13.write("This is appended line.\n")
file13.close()

# write a program to write n numeber of lines to the file and display all these lines as output. The number of lines to be written is to be taken as input from the user.
n = int(input("Enter number of lines to write to the file: "))
file14 = open("fileDemo2.txt", "w")
for i in range(n):
    line = input("Enter line: ")
    file14.write(line + "\n")
file14.close()
print("\n")
print("The content of the file is: ")
file14 = open("fileDemo2.txt", "r")
content14 = file14.read()
print(content14)
file14.close()
