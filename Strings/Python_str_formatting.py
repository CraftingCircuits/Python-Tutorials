# understanding string formatting in python
# F-Strings - F-string allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal, like this:
txt = f"Hello, my name is john."
print(txt)

# placeholders and modifiers - To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
age = 24
name = "john"
txt = f"Hello, my name is {name}. I am {age} years old."
print("\n")
print(txt)
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
price = 99
txt = f"Hello, my name is {name}. I am {age} years old. My hourly rate is {price:.2f} dollars."
print("\n")
print(txt)
# can also put the vaue directly without using a variable
txt = f"My hourly rate is {99:.2f} dollars."

# performing python operations in f strings - perform Python operations inside the placeholders.
txt = f"5 times 3 is equal to {5*3}."
print("\n")
print(txt)
# using variables in operations
a = 5
b = 4
c = 6
d = 2
txt = f"{a*b+c/d}"
print("\n")
print(txt)

# using if..else statements inside the placeholders
age = 15
txt = f"You are {'eligible' if age >= 18 else 'not eligible'} to vote."
print("\n")
print(txt)

# using built-in functions inside the placweholders
name = "john"
txt = f"{name.upper()}"
print("\n")
print(txt)


# using own functions inside the placeholders
def to_uppercase(x):
    return x.upper()


txt = f"{to_uppercase(name)}"
print("\n")
print(txt)

# understanding all the modifiers
# left aligns the result - :<
txt = f"Hello, my name is {name:<10}. I am Indian."
print("\n")
print(txt)
# right aligns the result - :>
txt = f"Hello, my name is {name:>10}. I am Indian."
print("\n")
print(txt)
# center aligns the result - :^
txt = f"Hello, my name is {name:^10}. I am Indian."
print("\n")
print(txt)
# places the sign to the left most position - := / this is used with numbers only
txt = f"Hello, my age is {age:=10}. I am Indian."
print("\n")
print(txt)
# use the plus sign to indicate if the numeber is positive or negative - :+
txt = f"Hello, my age is {age:+}. I am Indian."
print("\n")
print(txt)
# use minus sign for negative numbers only - :-
txt = f"Hello, my age is {age:-}."
print("\n")
print(txt)
txt = f"Hello, my age is {-13:-}."
print("\n")
print(txt)
# use space to leave a extra space for positive numbers - : (a space)
txt = f"Hello, my age is {age: }."
print("\n")
print(txt)
# use  a comma as a thousand separator - :,
txt = f"Hello, my age is {1000000:,}."
print("\n")
print(txt)
# use a underscore as a thousand separator - :_
txt = f"Hello, my age is {1000000:_}."
print("\n")
print(txt)
# binary format - :b
txt = f"Hello, my age is {age:b}."
print("\n")
print(txt)
# converts the value into unicode character - :c
txt = f"Hello, my age is {65:c}."
print("\n")
print(txt)
# decimal format - :d
txt = f"Hello, my age is {age:d}."
print("\n")
print(txt)
# scientific format, with a lower case e - :e
txt = f"Hello, my age is {age:e}."
print("\n")
print(txt)
# scientific format, with an uppercase E - :E
txt = f"Hello, my age is {age:E}."
print("\n")
print(txt)
# fix point number format - :f
txt = f"Hello, my age is {age:f}."
print("\n")
print(txt)
# fix point number format, with uppercase - :F
txt = f"Hello, my age is {age:F}."
print("\n")
print(txt)
# general format - :g
txt = f"Hello, my age is {age:g}."
print("\n")
print(txt)
# general format, with an uppercase - :G
txt = f"Hello, my age is {age:G}."
print("\n")
print(txt)
# octal format - :o
txt = f"Hello, my age is {age:o}."
print("\n")
print(txt)
# hex format, lowercase - :x
txt = f"Hello, my age is {age:x}."
print("\n")
print(txt)
# hex format, uppercase - :X
txt = f"Hello, my age is {age:X}."
print("\n")
print(txt)
# number format - :n
txt = f"Hello, my age is {age:n}."
print("\n")
print(txt)
# percentage format - :%
txt = f"Hello, my age is {age:%}."
print("\n")
print(txt)
# round to the nearest integer - :0
txt = f"Hello, my age is {age:0}."
print("\n")
print(txt)
# round to the nearest integer with 2 decimals - :.2
# txt = f"Hello, my age is {age:.2f}."
# print("\n")
# print(txt)
# txt = f"Hello, my age is {age:.3f}."
# print("\n")
# print(txt)
# round to the nearest integer with 2 decimals and a total of 10 characters - :10.2
# txt = f"Hello, my age is {age:10.2f}."
# print("\n")
# print(txt)
# round to the nearest integer with 2 decimals and a total of 10 characters, with comma as thousand separator - :,10.2
# txt = f"Hello, my age is {age:,10.2}."
# print("\n")
# print(txt)

# format method
# Add a placeholder where you want to display the price:
price = 99
txt = "The price is {} dollars."
print("\n")
print(txt.format(price))
# adding parameters inside the placeholder
txt = "The price is {:.2f} dollars."
print("\n")
print(txt.format(price))
# understanding multiple placeholders
age = 24
name = "john"
ans = True
txt = "Hello,  my name is {}. I am {} years ols. Am i Indian? {}"
print("\n")
print(txt.format(name, age, ans))
# placing the values in the correct order using index numbers
txt = "Hello, my name is {1}. i am {0} years old. Am i Indian? {2}"
print("\n")
print(txt.format(age, name, ans))
# using keyword arguments to make the code more readable
txt = "Hello, my name is {name}. i am {age} years ols. Am i Indian? {ans}"
print("\n")
print(txt.format(name=name, age=age, ans=ans))
