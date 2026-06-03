# json is a syntax for storing and exchanging data
# json is text, written with javascript notation
# python has built in function called json, which can be used to work with json data
import json

# using json.loads() method
x = '{"name": "Gaurav", "year": 2003, "age": 21}'
y = json.loads(x)
print(y["age"])

# converting python to json using dump() method
x = {"name": "Gaurav", "year": 2003, "age": 21}
y = json.dumps(x)
print("\n")
print(y)

# converting python objects to json strings
print("\n")
print(json.dumps({"name": "Gaurav", "year": 2003, "age": 21}))
print(json.dumps(("apple", "banana")))
print(json.dumps(["apple", "banana"]))
print(json.dumps("hell0"))
print(json.dumps(35))
print(json.dumps(52.35))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# converting python object containing all the legal data types
x = {
    "name": "Gaurav",
    "age": 21,
    "married": True,
    "divorced": False,
    "siblings": ("latika", "mrunal"),
    "pets": None,
    "cars": [{"model": "Porsche", "mpg": 29.5}, {"model": "lamborghini", "mpg": 14.7}],
}
print("\n")
print(json.dumps(x))
# using indent parameter to define the numbers of indents:
print("\n")
json.dumps(x, indent=3)
print(json.dumps(x))
# You can also define the separators, default value is (", ", ": "), which means using a
# comma and a space to separate each object, and a colon and a space to separate keys from values
print("\n")
json.dumps(x, indent=4, separators=(".", " = "))

# Use the sort_keys parameter to specify if the result should be sorted or not
json.dumps(x, indent=4, sort_keys=True)
print("\n")
print(json.dumps(x))
