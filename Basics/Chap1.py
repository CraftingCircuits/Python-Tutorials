# defining data types of python
# Numeric data types
# integer
a = 10
print(type(a))
# float
b = 10.05
print(type(b))
# complex
c = 2 + 3j
print(type(c))
# boolean
d = True
print(type(d))
# long
e = 1234835983409984509358
print(type(e))

# string data type
str1 = "Hello World"
print("\n")
print(type(str1))
str2 = "Python Programming"
print(type(str2))
str3 = """Python is a programming language"""
print(type(str3))
str4 = """Python is a programing language and affective"""
print(type(str4))

# list data type
list1 = [10, 20, 30, 40, 50]
print("\n")
print(type(list1))
list2 = ["Python", "java", "c++", "c#"]
print(type(list2))
list3 = [10, "Hello", 20.5, True, 30 + 2j]
print(type(list3))
list4 = []
print(type(list4))
list5 = list()
print(type(list5))
list6 = list("Hello")
print(type(list6))
print(list6)
list7 = list((10, 20, 30, 40))
print(type(list7))
print(list7)
list8 = list(range(1, 11))
print(type(list8))
print(list8)

# tuple data type
tuple1 = (10, 20, 30, 40, 50)
print("\n")
print(type(tuple1))
tuple2 = ("Python", "java", "c++", "c#")
print(type(tuple2))
tuple3 = (10, "hello", 20.5, True, 20 + 4j)
print(type(tuple3))
tuple4 = ()
print(type(tuple4))
tuple5 = tuple()
print(type(tuple5))
tuple6 = tuple("Hello")
print(type(tuple6))
print(tuple6)
tuple7 = tuple((10, 20, 30, 40))
print(type(tuple7))
print(tuple7)
tuple8 = tuple(range(1, 11))
print(type(tuple8))
print(tuple8)

# dictionary data type
dict1 = {"name": "john", "age": 25, "city": "new york"}
print("\n")
print(type(dict1))
dict2 = dict(name="john", age=25, city="new york")
print(type(dict2))
dict3 = {}
print(type(dict3))
dict4 = dict()
print(type(dict4))
dict5 = {1: "apple", 2: "banana", 3: "cherry"}
print(type(dict5))

#  Write a Python progran to perform addition of two numbers Accept the two numbers using keyboard
print("\n")
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = a + b
print("result:", c)

# Write a Python program to find the square root of a given number
print("\n")
import math

a = float(input("Enter a number:"))
result = a**0.5
print("Square root of", a, "is", result)

#  Write a program in Python to print aren and perimeter of a circle
print("\n")
radius = float(input("Enter the radius of the circle:"))
pi = 3.14159
area = pi * radius * radius
perimeter = 2 * pi * radius
print("Area of the circle is:", area)
print("Perameter of the circle is:", perimeter)

# Write a program to find area and perimeter of parallelogram
print("\n")
base = float(input("Enter the base of the parallelogram:"))
height = float(input("Enter the height of the parallelogram:"))
side = float(input("Enter the side of the parallelogram:"))
area = base * height
perimeter = 2 * (base + side)
print("Area of the parallelogram is:", area)
print("Peramater of the parallelogram is:", perimeter)

# Write a program to convert Fahrenheit to Celsius
print("\n")
fahrenheit = float(input("Enter temperature in fahrenheit:"))
celsius = (fahrenheit - 32) * 5.0 / 9.0
print("Temperature in celcius is:", celsius)

# Write a program in Python to convert  user inputs given time into minutes and secornds.
print("\n")
hours = int(input("Enter hours:"))
minutes = int(input("Enter minutes:"))
seconds = int(input("Enter seconds:"))
total_seconds = hours * 3600 + minutes * 60 + seconsds
print("Total time in seconds is:", total_seconds)
total_minutes = hours * 60 + minutes + seconds / 60
print("Total time in minutes is:", total_minutes)
