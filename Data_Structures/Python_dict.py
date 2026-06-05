# Python Dictionary
# dictionary is used to store data in key:value format
# dictionary is what, changeable, ordered, and don not allow duplicates
mydict = {"name": "John", "age": 22, "year": 2025}
print(mydict)

# printing specific value form the dictionary
print("\n")
print("printing specific value from dictionary")
mydict = {"name": "John", "age": 22, "year": 2025}
print(mydict["age"])

# duplicates are not allowed in dictionary
print("\n")
mydict = {"name": "John", "age": 22, "year": 2025, "year": 2002}
print(mydict)

# length of the dictionary
print("\n")
print("length of the dictionary")
mydict = {"name": "John", "age": 22, "year": 2025}
print(len(mydict))

# data type of the dictionary
print("\n")
print("type of the dictionary")
mydict = {
    "name": "John",
    "age": 22,
    "year": 2025,
    "condition": True,
    "colors": ["red", "blue", "green"],
}
print(type(mydict))

# using dict constructor to make a dictionary
print("\n")
print("constructing the dictionary")
mydict = dict(name="john", age=22, year=2025)
print(mydict)

# accessing items from the dictionary
print("\n")
print("accessing items from the dictionary")
mydict = {"name": "John", "age": 22, "year": 2025}
x = mydict["age"]
print(x)
# using get method to access item
x = mydict.get("age")
print(x)
# keys method to access key from dictionary
x = mydict.keys()
print(x)
# adding a key in the dictionary
mydict["color"] = "red"
print(x)
# printing all values from the dictionary
x = mydict.values()
print(x)
# changing value of a key in the dictionary
mydict["year"] = 2020
print(mydict)
# printing all items from the dictionary
x = mydict.items()
print(x)
# check if key exists
if "age" in mydict:
    print("John's age is right.")
# updating dictionary
mydict.update({"year": 2024})
print(mydict)
mydict.update({"name": "John"})
print(mydict)
# removing items from the dictionary
# pop() method will remove specified key item from the dictionary
mydict.pop("age")
print(mydict)
# popitem() will remove last inserted key item from the dictionary
mydict.popitem()
print(mydict)
# deleting a specific key item using del operator
del mydict["year"]
print(mydict)
# deleting whole dictionary using del operator
del mydict

# deleting whole dictionary using clear method
mydict = {"name": "John", "age": 22, "year": 2025}
mydict.clear()
print(mydict)

# looping dictionaries
# looping using for loop
print("\n")
print("looping dictionaries using for loop")
mydict = {"name": "John", "age": 22, "year": 2025}
for x in mydict:
    print(x)
print("\n")
for x in mydict:
    print(mydict[x])
print("\n")
for x in mydict.keys():
    print(x)
print("\n")
for x, y in mydict.items():
    print(x, y)

# copying one dictionary to another one
# copying dictionary using copy function
print("\n")
dict1 = {"name": "John", "age": 22, "year": 2025}
dict2 = {"state": "Gujarat", "district": "mehsana", "city": "Visnagar"}
print("copying dictionary using copy function")
dict1 = dict2.copy()
print(dict1)
# copying dictionary using dict function
print("copying dictionary using dict function")
dict1 = dict(dict2)
print(dict1)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
print("\n")
myCollection = {
    "car1": {"Model": "SUV-800", "Year": 2020},
    "car2": {"Model": "Mahindra", "Year": 2022},
    "car3": {"Model": "Lambo", "Year": 2023},
}
print(myCollection)
# creating dictionaries in other way
print("\n")
car1 = {"Model": "SUV-800", "Year": 2020}
car2 = {"Model": "Mahindra", "Year": 2022}
car3 = {"Model": "Lambo", "Year": 2023}
myCollection = {"car1": car1, "car2": car2, "car3": car3}
print(myCollection)

# accessoing items from dictionary
# accessing items in nested dictionary
print("\n")
myCollection = {
    "car1": {"Model": "SUV-800", "Year": 2020},
    "car2": {"Model": "Mahindra", "Year": 2022},
    "car3": {"Model": "Lambo", "Year": 2023},
}
print(myCollection["car2"]["Model"])

# loop through nested dictionary
print("\n")
for x, car in myCollection.items():
    print(x, car)

    for y in car:
        print(y + ":", car[y])
