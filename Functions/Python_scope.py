# A variable is only available from inside the region it is created. This is called scope.
# local scope
def my_fun():
    x = 10
    print(x)


my_fun()


# function inside the function
print("\n")


def my_fun():
    x = 10

    def my_inner_fun():
        print(x)

    my_inner_fun()


my_fun()


# global scope
print("\n")
x = 10


def my_fun():
    print(x)


my_fun()
print(x)

# naming variables, if you name variables as same inside a function and also same outside the function,
# python will treat them as twp separate variables. one vailable in the global scope and one in the local scope.
print("\n")
x = 10


def my_fun():
    x = 20
    print(x)


my_fun()
print(x)

# global keyword
print("\n")
x = 10


def my_fun():
    global x
    x = 20
    print(x)


my_fun()
print(x)

# nonlocal keyword
print("\n")


def my_fun1():
    x = "Riya"

    def my_fun2():
        nonlocal x
        x = "Tiya"

    my_fun2()
    return x


print(my_fun1())
