# write a program that makes use of multiple exceptions for accepting the positive value only. if user enters negative or zero value then exception is raised
class Error(Exception):
    """Base class for other exceptions"""

    pass


class NegativeValue(Error):
    """Raised when the input value is negative"""

    pass


class ZeroValue(Error):
    """Raised when the input value is zero"""

    pass


while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < 0:
            raise NegativeValue
        elif i_num == 0:
            raise ZeroValue
        break
    except (NegativeValue, ZeroValue):
        print("Invalid Data!. Enter positive value")
        print()
print("Good, You have entered positive value")


# write a python program to count number of vowels and consonants present in the text files.
input_file = open("test.txt", "r")
vowels = set("AEIOUaeiou")
cons = set("bcdfghjklmnpqrstvwxysBCDFGHJKLMNPQRSTVWXYZ")
count_vowels = 0
count_cons = 0
for c in input_file.read():
    if c in vowels:
        count_vowels += 1
    elif c in cons:
        count_cons += 1
print("\n")
print("Number of vowels in a file are: ", count_vowels)
print("Number of consonants in a file are: ", count_cons)
input_file.close()


# write a python program to count total number of words in a file.
count = 0
with open("test.txt", "r") as f:
    for line in f:
        word = line.split()
        count += len(word)
f.close()
print("\n")
print("Total number of words in file are: ", count)


# write a python program to count total number of characters in a file
count = 0
with open("test.txt", "r") as file:
    for line in file:
        word = line.split()
        count += len(line)
file.close()
print("\n")
print("Total number of characters in file are: ", count)


# write a python program to count total number of blank spaces in a file
with open("test.txt", "r") as f:
    count = 0
    for line in f:
        word = line.split()
        for letter in word:
            if letter.isspace:
                count += 1
print("\n")
print("Total number of blank spaces are: ", count)


# write a python program to write the contents of one file to another file from end.
lines = []
with open("test.txt", "r") as f:
    lines = f.readlines()
f.close()
with open("reversed_file.txt", "w") as f:
    for line in reversed(lines):
        f.write(line)
f.close()
