# file handling in python
# the open() function takes two parameters: filename and mode
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
f = open("demofile.txt")
print(f.read())
f = open("demofile.txt")
print(f.read())
f = open("demofile.txt", "r")

# using with statement
with open("demofile.txt") as f:
    print(f.read())

# closing the file
f = open("demofile.txt")
print(f.readline())
f.close()

# read only parts of the file
with open("demofile.txt") as f:
    print(f.read(5))

# reading the lines
with open("demofile.txt") as f:
    print(f.readline())

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

with open("demofile.txt") as f:
    for x in f:
        print(x)


# writing to an existing file
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

print("\n")
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

# open and read the file after the appending:
print("\n")
with open("demofile.txt") as f:
    print(f.read())

# overwriting an existing content using "w" mode
print("\n")
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

# open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())


# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists
# f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")
# f = open("myfile.txt", "a")

# To delete a file, you must import the OS module, and run its os.remove() function:
import os

os.remove("demofile.txt")


# check if file exists, then delete it
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
