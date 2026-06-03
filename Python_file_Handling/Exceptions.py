# single exceptions
# try-Except statement - perform division of two numbers
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
except ValueError:
    print("You have entered wrong data.")
except ZeroDivisionError:
    print("Divide by zero error!")
else:
    print("The result is: ", c)


# Raise statement - define negative number
num = int(input("Enter value for num: "))


def NegativeNum(num):

    if num < 0:
        print("Number is negative. ")
        # raise ValueError("Number is negative!")
    else:
        print("Number is positive. ")


print(NegativeNum(num))
