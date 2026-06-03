# None is a special constant in Python that represents the absence of a value.
# Its data type is NoneType, and None is the only instance of a NoneType object.
# Variables can be assigned None to indicate "no value" or "not set"
x = None
print(x)
print(type(x))

# comparing to None
print("\n")
if x is None:
    print("x is None")
else:
    print("x is not None")

# true or false
print("\n")
print(bool(x))


# functions returning None
def func():
    x = 5


x = func()
print("\n")
print(x)


def func2():
    return None


x = func2()
print("\n")
print(x)

# user inputs
print("\n")
print("Enter your name:")
name = input()
print("Hello," + name)

# using prompt in input function
print("\n")
age = input("Enter your age: ")
print(age)

# multiple inputs
print("\n")
a, b = input("Enter two numbers separated by space: ").split()
print("First number:", a)
print("Second number:", b)
fav = input("Enter your favorite color: ")
fav1 = input("Enter your favorite food: ")
fav2 = input("Enter your favorite movie: ")
fav3 = input("Enter your favorite sport: ")
print(fav, fav1, fav2, fav3)

# input numbers
x = int(input("Enter a numbers: "))
print(x)

# validate input
y = True
while y == True:
    x = input("Enter a number: ")
    try:
        x = float(x)
        y = False
    except:
        print("Please try again.")
print("get out")
