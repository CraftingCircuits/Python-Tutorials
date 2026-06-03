# Python Arithmetic Operators
# Addition
print(5+3)
# Subtraction
print(5-3)
# Multiplication
print(5*3)
# Division
print(5/3)
# Modulus
print(5%3)
# Exponentiation
print(5**3)
# Floor division
print(5//3)

# Python Assignment Operators
# Assign
# x = int(x)
x = 5
print(x)
# Add and assign
x += 3
print(x)
# Subtract and assign
x -= 3
print(x)
# Multiply and assign\
x *= 3
print(x)
# divide and assign
x /= 3
print(x)
# Modulus and assign
x %= 3
print(x)
# Exponetiation and assign
x **= 3
print(x)
# Floor division and assign
x //= 3
print(x)
# and assign
x = int(x)
x &= 3
print(x)
# or assign
x |= 3
print(x)
# xor assign
x ^= 3
print(x)
# right shift and assign
x >>= 3
print(x)
# left shift and assign
x <<= 3
print(x)

# Python Comparison Operators
x = 2
y = 3
# not equal and assign
print(x != y)
# Equal and assign
print(x == y)
#  greater than
print(x > y)
# Less than
print(x < y)
# Greater than or equal to
print(x >= y)
# Less than or equal to
print(x <= y)

# Python Logical Operators
# and operator
if (x > 3 and x < 10):
    print("x is between 3 and 10")
# or operator
if (x < 3 or x > 10):
    print("x is either less than 3 or greater than 10")
# not operator
if not(x==3):
    print("x is not equal to 3")

# Python Identity Operators
# is operator
x = [1,2,3]
y = [1,2,3]
if x is y:
    print("x is y")
# is not operator
if x is not y:
    print("x is not y")
    
# Python membership operators
# in operator
x = [1,2,3]
if 1 in x:
    print("1 is in x")
# not in operator
if 4 not in x:
    print("4 is not in x")

# Python Bitwise operators
# Bitwise AND
x = 5
y = 3
print(x & y)
# Bitwise OR
print(x | y)
# Bitwise XOR
print(x ^ y)
# Bitwise NOT
print(~x)
# Bitwise left shift
print(x << 1)
# Bitwise right shift
print(x >> 1)

# Sequence of precedence Operators
# 1. Parentheses
# 2. Exponentiation
# 3. Unary plus and minus
# 4. Multiplication, division, floor division, and modulus
# 5. Addition and subtraction
# 6. Bitwise shift operators
# 7. bitwise AND
# 8. bitwise XOR
# 9. bitwise OR
# 10. Comparison operators
# 11. Identity operators
# 12. Membership operators
# 13. logical operators
x = (5 + 3) * 2 ** 2 > 15 and not (4 < 2)
print(x)
