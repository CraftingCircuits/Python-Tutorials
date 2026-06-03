# consider a module to be a code library, that contains a set of functions that you want to add in your application.
# creating a module, first make a file with .py extension and then write the code in it.
# now calling the module in this file
import myModule

# now calling the function from the module
myModule.greeting(("Niyati"))

# the module can contain multiple functions as well as variables, such as arrays, dictionaries, objects etc.
# calling the variables from the module
print("\n")
print("list from the module:")
print(myModule.my_list)
print("\n")
print("set from the module:")
print(myModule.my_set)
print("\n")
print("tuple from the module:")
print(myModule.my_tuple)
print("\n")
print("dictionary from the module:")
print(myModule.my_dict)
print("\n")
print("string from the module:")
print(myModule.my_string)
print("\n")
print("number from the module:")
print(myModule.my_number)
print("\n")
print("boolean from the module:")
print(myModule.my_boolean)
print("\n")
print("complex function from the module:")
print(myModule.my_fun(1, 2, 3, 4, 5))
print("\n")
print("sorted numbers from the module:")
print(myModule.sorted_numbers(5, 4, 3, 2, 1))
print("\n")
print("largest numbers from the module:")
print(myModule.largest_numbers(5, 4, 3, 2, 1))

# renaming a module
import myModule as mm

# now calling the function from the renamed module
print("\n")
mm.greeting(("Niyati"))
# calling the variables from the renamed module
print("\n")
print("Dictionary from the renamed module:")
print(mm.my_dict)
print("\n")
print("largest numbers from the renamed module:")
print(mm.largest_numbers(12, 542, 2, 34, 128))

# using built in modules in python
# understanding the system module
import sys

# printing the version of python
print("\n")
print("Python version:", sys.version)
# using the math module
import math

# printing the square root of a number
print("\n")
a = 16
print("square root of", a, "is:", math.sqrt(a))
# using the operating system interface module
import os

# printing the current working directory
print("\n")
print("Current working directory:", os.getcwd())
# using the random module
import random

# printing a random number between 1 and 10
print("\n")
print("Random number between 1 and 10:", random.randint(1, 10))
# using the datetime module
import datetime

# printing the current date and time
print("\n")
print("Current date and time", datetime.datetime.now())
# using the time module
import time

# printing the current time
print("\n")
print("Current time:", time.strftime("%H:%M:%S"))
# using the statistics module
import statistics

# prinitng the mean of a list of numbers
print("\n")
numbers = [1, 2, 3, 4, 5]
print("Mean of the list of numners:", statistics.mean(numbers))
# using the json module
import json

# creating a dictionary
data = {"Name": "Niyati", "Age": 20, "City": "Mumbai", "Born": 2006}
# converting the dictionary to a json string
json_data = json.dumps(data)
# printing the json string
print("\n")
print("JSON data:", json_data)
# using the calendar module
import calendar

# printing the calendar of the current month
print("\n")
print("Calendar of the current month:")
print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))

# using functools module
import functools


# defining a function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(
    input("Enter a number to calculate its factorial: ")
)  # You can set n to any positive integer
factorial = functools.reduce(lambda x, y: x * y, range(1, n + 1))
print("Factorial of", n, "using functools.reduce is:", factorial)

# using the itertools module
import itertools


# defining a function to generate permutations of a list
def generate_permutations(lst):
    return list(itertools.permutations(lst))
