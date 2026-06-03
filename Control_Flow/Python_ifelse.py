# python if else statements with basic conditions
# defined variables and conditions
x = 24
if x > 25:
    print("X is greater than 25.")
elif x <= 25:
    print("X is less than or equal to 25.")
print("\n")
# undefined variables and conditions, asking from users and applying if else statements
# print("Enter a number: ")
# num = int(input())
# if num % 2 == 0:
#     print("Your number is even.")
# elif num % 2 != 0:
#     print("Your number is odd.")
# else:
#     print("Enter valid number.")

# short hand if else statements
x = 16
if x > 15:
    print("X is greater than 15.")
# short hand if else statements
x = 16
print("YES") if x > 15 else print("NO")

# using logical operators AND, OR, XOR
x = 15
y = 20
z = 25
if x % 5 == 0 and y % 5 == 0 and z % 5 == 0:
    print("all numbers all divisible by 5.")
if x % 2 == 0 or y % 2 == 0:
    print("one of the number is even.")
if not x > y:
    print("X is not greater than y.")

# understanding nested if else statements
a = 50
if a > 45:
    print("is greater than 45.")
    if a % 5 == 0:
        print("is also divisible by 5.")
    else:
        print("is not divisible by 5.")

# understanding the pass statement, when you have nothing to put in if statements,
# if you have not any content for it, you can simply write pass statement to avoid getting an error
a = 3
b = 5
if b > a:
    pass
