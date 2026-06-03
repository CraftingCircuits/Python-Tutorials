# Python functions, which are defined by def word and have parameters with parenthesis,
# we can pass data as parameters in a function and it returns data as result.
# creating a funtion
def myCollection():
    print("Congratulations for your new porshe.")


# calling a function
def myCollection():
    print("Congratulations for your new porshe.")


myCollection()
print("\n")


# understanding arguments in function, you can add arguments after function in parenthesis,
# and if you want to add more, just separate them with a comma,information can be passed into a function asarguments
def myCollection(greetings):
    print(greetings + " " + "Congratulations for your new porshe.")


myCollection("Hey!! ")
myCollection("Woooowwww ")
myCollection("Niicceee ")


# in Python, parameters and arguments are same things to pass any information in a function,
# but in function's perspective, a parameter ia variable listed inside the parentheses in the function definition
# and arguments are the value that is sent to the function when it is called.
# number of arguments - a function must be called with correct number of arguments
print("\n")


def myCars(Model, num):
    print(Model + " " + num)


myCars("Thar", "2006")


# arbitary argumnets, If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
print("\n")


def myNames(*name):
    print("Your name is " + name[2])


myNames("Piya", "Riya", "Diya", "Tiya")

# keyword arguments are also allowed in python, we can add it by key = value syntax
print("\n")


def myNames(name1, name2, name3):
    print("You are my " + name2)


myNames(name1="Ravi", name2="Hunny", name3="Bunny")

# arbitary keyword arguments, f you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
print("\n")


def myNames(**name):
    print("You are my " + name["name2"])


myNames(name1="Ravi", name2="Hunny", name3="Bunny")

# default parameter value
print("\n")


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# passing an list as an arguments, You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
print("\n")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# return values from function
print("\n")


def my_function(x):
    return x / 2


print(my_function(22))
print(my_function(40))


# pass statements - if we have no content with function definition
def my_function():
    pass


# positional only arguments, add / after the function's argument
print("\n")


def myFunction(x, /):
    print(x)


myFunction(3)

# combined positional only and keyword only
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
print("\n")


def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)


# understanding recursions in a function
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(2)
