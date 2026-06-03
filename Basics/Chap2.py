# write a python program to check whether a given number is even or odd
# using only if statement
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is even")
# if num % 2 != 0:
#     print(num, "is odd")

# using if else statement
# print("\n")
# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

# write a program to compare to numbers using nested conditions
# print("\n")
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# if a == b:
#     print("Both are equal")
# else:
#     if a > b:
#         print("a is greater than b")
#     else:
#         if a < b:
#             print("a is less than b")

# # write a python program to display the result such as distinction, first class, second class, pass or fail based on the marks obtained by the student
# print("\n")
# marks = int(input("Enter your marks:"))
# if marks >= 75:
#     print("Distinction")
# elif marks >= 60:
#     print("First class")
# elif marks >= 50:
#     print("Second class")
# elif marks >= 35:
#     print("Pass")
# elif marks < 35:
#     print("Fail")
# else:
#     prin("Invalid input")

# # write a python program to find the largest among the three numbers
# print("\n")
# a = int(input("Enter first number:"))
# b = int(input("Enter second numebr:"))
# c = int(input("Enter third number:"))
# if a >= b and a >= c:
#     print("C is the largest number")
# elif b >= a and b >= c:
#     print("b is the largest number")
# elif c >= a and c >= b:
#     print("c is the largest number")
# else:
#     print("Invalid input")

# write the python program for computing the sum of n natural numbers and finding out the average of it using while loop
# print("\n")
# n = int(input("Enter a number how many natural numbers you want to add:"))
# sum = 0
# average = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print("Sum is:", sum)
# average = sum / n
# print("Average is:", average)

# write a python program to display square of n numbers using while loop
# print("\n")
# n = int(input("Enter a number how many squares of numbers you want to display:"))
# i = 1
# while i <= n:
#     print("square of", i, "is:", i**2)
#     i = i + 1

# write a python program to display even or odd numbers between i to n using while loop
# print("\n")
# n = int(input("Enter a number upto which you want to display even or odd numbers:"))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")
#     i = i + 1

# write a python program to display fibonacci numbers for the sequense of length n using while loop
# print("\n")
# n = int(input("Enter a number how many fibonacci numbers you want to display:"))
# a = 0
# b = 1
# i = 0
# print("Fibonacci sequence is:")
# while i < n:
#     print(a)
#     # print(b)
#     c = a + b
#     a = b
#     b = c
#     i = i + 1

# write a python program to display the star pattern using for loop
# *
# * *
# * * *
# * * * *
# print("\n")
# n = int(input("Enter a number of rows you want to display star pattern:"))
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print("\n")

# write a python program to display the star pattern using for loop
# * * * *
# * * *
# * *
# *
# print("\n")
# n = int(input("Enter a number of rows you want to display star pattern:"))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print("\n")

# write a python program to display the star pattern using for loop
#   *
#  * *
# * * *
#  * *
#   *
# print("\n")
# n = int(input("Enter a number of rows you want to display star pattern:"))
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)

# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)

# write a python program to display numbers pattern using for loop
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
print("\n")
n = int(input("Enter a number of rows you want to display number pattern:"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")

# write a python program to display numbers pattern using for loop
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4
print("\n")
n = int(input("Enter a number of rows you want to display number pattern:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")
