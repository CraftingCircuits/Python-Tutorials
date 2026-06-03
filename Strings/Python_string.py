string = "Hello World"
# converts the first character to uppercase
print(string.capitalize())
# convert string into lower case
print(string.casefold())
# returns a centered string
print(string.center(90))
# returns the number of times a specified value occurs in a string
print(string.count("l"))
# returns an encoded version of the string
print(string.encode())
# returns True if the string ends with the specified value
print(string.endswith("world"))
# sets the tab size of the string
print(string.expandtabs(4))
# searches the string for a specified value and returns the position of where it was found
print(string.find("World"))
# formats specified values in a string
print(string.format_map("Python"))
# searches the string for a specified value and returns the position of where it was found
print(string.index("World"))
# returns True if all characters in the string are alphanumeric
print(string.isalnum())
# return True if all characters in the string are alphabetic
print(string.isalpha())
# returns True if all characters in the string are ascii characters
print(string.isascii())
# returns True if all characters in the string are decimal characters
print(string.isdecimal())
# returns True if all characters in the string are digits
print(string.isdigit())
# returns True if all characters in the string is an identifier
print(string.isidentifier())
# returns True if all characters in the string are in lowercase
print(string.islower())
# returns True if all characters in the string are numeric
print(string.isnumeric())
# returns True if all characters in the string are printable
print(string.isprintable())
# returns True if all characters in the string are whitespace characters
print(string.isspace())
# returns True if all characters in the string are in title case
print(string.istitle())
# returns True if all characters in the string are uppercase
print(string.isupper())
# returns a left justified version of the string
print(string.ljust(90, '*'))
# Converts a string into lower case
print(string.lower())
# returns a left trim version of the string
print(string.lstrip())
# Returns a translation table to be used in translations
print(string.maketrans("H","J"))
# Returns a tuple where the string is parted into three parts
print(string.partition("World"))
# Returns a string where a specified value is replaced with a specified value
print(string.replace("World", "Python"))
# Searches the string for a specified value and returns the last position of where it was found
print(string.rfind("l"))
# Searches the string for a specified value and returns the last position of where it was found
print(string.rindex("l"))
# returns a right justified version of the string
print(string.rjust(50, '*'))
# Returns a tuple where the string is parted into three parts
print(string.rpartition("World"))
# Splits the string at the specified separator, and returns a list
print(string.rsplit(" "))
# Returns a right trim version of the string
print(string.rstrip())
# Splits the string at the specified separator, and returns a list
print(string.split(","))
# split the string at line breaks and returns a list
print(string.splitlines())
# Returns True if the string starts with psecified value
print(string.startswith("Hello"))
# returns a trimed version of the string
print(string.strip())
# Swaps cases, lowerase becomes uppercase and vice versa
print(string.swapcase())
# Converts the first character of each word to upper case
print(string.title())
# Returns a translated string, where each character is mapped to its corresponding value in the translation table
print(string.translate(string.maketrans("H", "J")))
# Converts a string into uppercase
print(string.upper())
# Fills the string with a specified number of 0 values at the beginning
print(string.zfill(50)) 

