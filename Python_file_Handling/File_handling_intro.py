# 'r' - open file for reading
# 'w' - open file for writing
# 'x' - create file for creation only
# 'a' - open file for appending
# 't' - opens file in text mode
# 'b' - opens file in binary mode
# '+' - opens file for updation reading or writing

# write a program to read the contents of the file named 'test.txt'
file1 = open("fileDemo1.txt", "r")
content = file1.read()
print(content)
# we can also write it directly - print(file1.read())
file1.close()


# write a program to read and display first two lines of the text file
file2 = open("fileDemo1.txt", "r")
line1 = file2.readline()
line2 = file2.readline()
print("\n")
print(line1)
print(line2)
file2.close()

# write a program to read and display all the lines of the text file
file3 = open("fileDemo1.txt", "r")
lines = file3.readlines()
print("\n")
for line in lines:
    print(line)
file3.close()

# write a program to display the contents of the file as list
file4 = open("fileDemo1.txt", "r")
lines_list = file4.readlines()
print("\n")
print(lines_list)
file4.close()

# it can also be done in a single line code
print("\n")
print(list(content))
print("\n")
print(list(line1))
print("\n")
print(list(lines))
print("\n")
print(list(lines_list))


# opening the file using with statement
with open("fileDemo1.txt", "r") as file5:
    content5 = file5.read()
    print("\n")
    print(content5)
file5.close()


# write a python program to find the line that starts with the word "This" from the following text which is stored in a file,
# This is a python program.
# python is superb.
# This is third line of program.
# this python program is nice.

file6 = open("fileDemo1.txt", "r")
lines6 = file6.readlines()
print("\n")
for line in lines6:
    if line.startswith("This"):
        print(line)
file6.close()

# it can also be done using rstrip() function to avoid extra spaces
file7 = open("fileDemo1.txt", "r")
lines7 = file7.readlines()
i = 0
print("\n")
for line in lines7:
    line = line.rstrip()
    if line.find("This") == -1:
        continue
    print(line)
    i += 1
file7.close()

# it can also be done using with statement
with open("fileDemo1.txt", "r") as file8:
    lines8 = file8.readlines()
    print("\n")
    for line in lines8:
        if line.startswith("This"):
            print(line)
            file8.close()


# write a program to split the text line written in the file into words
file9 = open("fileDemo1.txt", "r")
lines9 = file9.readlines()
print("\n")
for line in lines9:
    words = line.split()
    print(words)
file9.close()

# it can also be done using with statement
with open("fileDemo1.txt", "r") as file10:
    line10 = file10.readline()
    words10 = line10.split()
    print("\n")
    print(words10)
file10.close()
