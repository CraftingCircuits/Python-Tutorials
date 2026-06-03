# lambda function is a small anonymous function
# it can take any number of arguments, but can only have one expression
# syntax: lambda arguments : expression
x = lambda a: a + 10
print(x(50))

# labda function with multiple arguments
y = lambda a, b, c, d, e: a / b * c + d - e
print(y(10, 2, 3, 5, 7))


# the power of lambda functions is when you use it inside the functions
def my_fun(n):
    return lambda a: a * n


print(my_fun(5)(6))


# lambda function with filter
def my_filter(x):
    return x > 10


numbers = [
    35,
    12,
    9,
    45,
    94,
    2,
    11,
    7,
    3,
    75,
    69,
    29,
]
filtered_numbers = list(filter(my_filter, numbers))
print("Filtered numbers:")
print(filtered_numbers)

# lambda function with map
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:")
print(squared_numbers)

# lambda function with reduce
from functools import reduce


def my_reduce(x, y):
    return x + y


reduced_value = reduce(my_reduce, numbers)
print("Reduced value (sum):")
print(reduced_value)

# lambda function with sorted
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted numbers:")
print(sorted_numbers)
