# Python RegEx module, regular expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# python has a built in package called re, which can be used to work with regular expressions.
import re

txt = "The rain is starting soon"
x = re.search("^The.*soon$", txt)

if x:
    print("Yes, we have a match!")
else:
    print("Sorry..")

# re module offers a set of functions that allows us to search a string for a match
# using match function - check for a match begining of a string only
txt1 = "Hello World"
result = re.match(r"Hello", txt1)
print("\n")
print(result.group())

# using search function - searches the entire string of the first match
txt2 = "Say Hello to the world"
result = re.search(r"Hello", txt2)
print("\n")
print(result.group())

# using findall function - returns a list containing all matches
txt3 = "Ritesh is very hardworking guy. He is allrounder. he works so much. he also plays sports."
result = re.findall(r"He", txt3)
print("\n")
print(result)

# using finditer - returns an iterator yeilding match for al objects
txt4 = "hello says his fello classmates to cello"
matches = re.finditer(r"\b\w{5}\b", txt4)
print("\n")
for match in matches:
    print(match.group())

# using sub() function - Substitutes matches with a replacement string
txt5 = "I love Dogs, Dogs are amazing"
new_txt = re.sub(r"Dogs", "Cats", txt5)
print("\n")
print(new_txt)

# using split function - splits the string by a matched pattern
text = "one, two; three four"
result = re.split(r"[;,\s]+", text)
print("\n")
print(result)  # Output: ['one', 'two', 'three', 'four']

# using compile compile a regular expression pattern into a reusable object
pattern = re.compile(r"\d+")
result = pattern.findall("There are 12 cats and 4 dogs.")
print("\n")
print(result)  # Output: ['12', '4']

# understanding all metacharacters
# a set of characters []
element = "Your name is Rahul."
x = re.findall("[a-z]", element)
print("\n")
print(x)

# signals a special sequence
element = "Your body count is 15. how much its in $?"
x = re.findall("\d", element)
print("\n")
print(x)

# any character except new line character
element = "Hello World"
x = re.findall("He..o", element)
print("\n")
print(x)
y = re.findall("He..d", element)
print(y)

# starts with
element = "You are beautiful"
x = re.findall("You", element)
print("\n")
if x:
    print("Yes, it starts with you.")
else:
    print("no match!")

# ends with
element = "You are beautiful"
x = re.findall("beautiful$", element)
print("\n")
if x:
    print("Yes, it ends with it.")
else:
    print("No match!")

# zero or more occurance
element = "You are rich"
x = re.findall("Yo.*e", element)
print("\n")
print(x)

# one or more occurance
element = "You are rich"
x = re.findall("Yo.+e", element)
print("\n")
print(x)

# zero or one occurance
element = "You are rich"
x = re.findall("Yo.?e", element)
print("\n")
print(x)
# This time we got no match, because there were not zero, not one, but three characters between "Yo" and the "e"

# exactly the specified number of occurrence (e.g., exactly 3 characters between "Yo" and "e")
element = "You are rich"
x = re.findall("Yo.{3}e", element)
print("\n")
print(x)

# either or
element = "You are a very string girl. you are very brave and self worthy.!"
x = re.findall("brave|self", element)
print("\n")
print(x)
if x:
    print("Yes it matches")
else:
    print("Next time!")

# capture and group
element = "You are a very strong man."
x = re.findall("(strong|brave)", element)
print("\n")
print(x)
if x:
    print("Yes it matches")
else:
    print("Next time!")

# adding expression flags
# using re.ASCII flag
element = "You are very beautiful."
x = re.findall("\w", element, re.ASCII)
print("\n")
print(x)

# using re.debug flag
element = "You are very beautiful"
x = re.findall("\w", element, re.DEBUG)
print("\n")
print(x)

# using re.dotall flag
element = "You are very beautiful. \nYou are also very kind."
x = re.findall("You.*kind", element, re.DOTALL)
print("\n")
print(x)

# using re.ignorecase flag
element = "You are very beautiful. You are also very kind."
x = re.findall("you", element, re.IGNORECASE)
print("\n")
print(x)

# using re.multiline flag
element = "You are very beautiful.\nYou are also very kind."
x = re.findall("^You", element, re.MULTILINE)
print("\n")
print(x)

# using re.noflag flag
element = "You are very beautiful. \nYou are also very kind."
x = re.findall("You", element, re.NOFLAG)
print("\n")
print(x)

# using re.unicode flag
element = "You are very beautiful. \nYou are also very kind."
x = re.findall("\w", element, re.UNICODE)
print("\n")
print(x)

# using re.verbose flag
element = "You are very beautiful. \nYou are also very kind."
x = re.findall(
    r"""
               You
               \s+
               are
               \s+
               very
               \s+
               """,
    element,
    re.VERBOSE,
)
print("\n")
print(x)

# understanding special sequences
# \A - matches only at the beginning of the string
element = "Hello World"
x = re.findall(r"\AHello", element)
print("\n")
print(x)

# \b - matches the empty string at the beginning or end of a word
element = "Hello World"
x = re.findall(r"\bWorld", element)
print("\n")
print(x)

# \d - matches any digit character
element = "There are 12 cats and 4 dogs."
x = re.findall(r"\d", element)
print("\n")
print(x)

# \D - matches any non-digit character
element = "There are 12 cats and 4 dogs."
x = re.findall(r"\D", element)
print("\n")
print(x)

# \s - matches any whitespace character
element = "Hello World"
x = re.findall(r"\s", element)
print("\n")
print(x)

# \S - matches any non-whitespace character
element = "Hello World"
x = re.findall(r"\S", element)
print("\n")
print(x)

# \w - matches any alphanumeric character (including underscore)
element = "Hello World"
x = re.findall(r"\w", element)
print("\n")
print(x)

# \W - matches any non-alphabetic character
element = "Hello World"
x = re.findall(r"\W", element)
print("\n")
print(x)

# \Z - matches only at the end of the string
element = "Hello World"
x = re.findall(r"\Z", element)
print("\n")
print(x)

# \n - matches a newline character
element = "Hello \nWorld"
x = re.findall(r"\n", element)
print("\n")
print(x)

# understanding sets - a set is a characters inside a pair of square brackets [] with a special meaning
# [arn] - matches any character a, r or, n
element = "Hello World"
x = re.findall(r"[arn]", element)
print("\n")
print(x)

# [a-z] - matches any lowercase letter from a to z
element = "Hello World"
x = re.findall(r"[a-z]", element)
print("\n")
print(x)

# [A-Z] - matches any uppercase letter from A to Z
element = "Hello World"
x = re.findall(r"[A-Z]", element)
print("\n")
print(x)

# [0-9] - matches any digit from 0 to 9
element = "There are 12 cats and 4 dogs."
x = re.findall(r"[0-9]", element)
print("\n")
print(x)

# [^arn] - matches any character except a, r or, n
element = "Hello World"
x = re.findall(r"[^arn]", element)
print("\n")
print(x)

# [a-zA-Z] - matches any letter, either lowercase or uppercase
element = "Hello World"
x = re.findall(r"[a-zA-Z]", element)
print("\n")
print(x)

# understanding findall function
# findall function returns a list containing all matches
import re

text = "The India is all time favourite country of mine."
x = re.findall("all", text)
print("\n")
print(x)

# in the list, if no matches are found, an empty list is returned
text2 = "The India is all time favourite country of mine."
x2 = re.findall("none", text2)
print("\n")
print(x2)

# the search function returns a match object, which contains information about the match
# function searches the string for a match, and returns a Match object if there is a match.
text3 = "The India is all time favourite country of mine."
x3 = re.search("favourite", text3)
print("\n")
print(x3)
print("\n")
print(x3.group())

# if no match is foundm it returns None
text4 = "The India is all time favourite country of mine."
x4 = re.search("none", text4)
print("\n")
print(x4)

# the split function returns a list where the string has been split at each match:
text5 = "The India is all time favourite country of mine."
x5 = re.split(" ", text5)
print("\n")
print(x5)

# you can control the number of occurrences by specifying the maxsplit parameter:
text6 = "The India is all time favourite country of mine."
x6 = re.split(" ", text6, maxsplit=2)
print("\n")
print(x6)

# split the strig only atthe first occurance of the match
text7 = "The India is all time favourite country of mine."
x7 = re.split(" ", text7, maxsplit=1)
print("\n")
print(x7)

# the sub function replaces the matches with the text of your choice:
text8 = "The India is all time favourite country of mine."
x8 = re.sub("favourite", "most loved", text8)
print("\n")
print(x8)

# we can control the number of replacements by specifying the count parameter:
text9 = "The India is all time favourite country of mine. My favourite food is misal pav. My favourite drink is coffee."
x9 = re.sub("favourite", "most loved", text9, count=2)
print("\n")
print(x9)

# the match object is the object containing the information about the search and the result.
text10 = "The India is all time favourite country of mine."
x10 = re.search("favourite", text10)
print("\n")
print(x10)
print("\n")
print(x10.group())

# .span() returns a tuple containing the start-, and end positions of the match.
text11 = "The India is all time favourite country of mine."
x11 = re.search("favourite", text11)
print("\n")
print(x11.span())
print("\n")
print(x11.start())
print("\n")
print(x11.end())

# .string returns the string passed into the function
text12 = "The India is all time favourite country of mine."
x12 = re.search("favourite", text12)
print("\n")
print(x12.string)
# .group() returns the part of the string where there was a match
print("\n")
print(x12.group())
