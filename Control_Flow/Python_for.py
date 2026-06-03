# understanding for loop in python, it can be eaither in list, array, tuple, set, dictionary or in string
# for list, set and dictionary
friuts = ["apple", "banana", "cherry"]
for item in friuts:
    print(item)

print("\n")
cars = ["suv", "audi", "BMW"]
for item in cars:
    print(item)

print("\n")
toys = ("barbie", "car", "robot")
for item in toys:
    print(item)

print("\n")
mySongs = {"lofi": "love me", "piece": "choudhary", "year": 2020}
for item in mySongs.keys():
    print(item)
for item in mySongs.items():
    print(item)

print("\n")
for x in "Watermelon":
    print(x)

# understanding break and continue statemnets in for loop
print("\n")
friuts = ["apple", "banana", "cherry"]
for item in friuts:
    print(item)
    item == "banana"
    break
# also can write like this
friuts = ["apple", "banana", "cherry"]
for item in friuts:
    if item == "banana":
        break
    print(item)


print("\n")
friuts = ["apple", "banana", "cherry"]
for item in friuts:
    print(item)
    item == "banana"
    continue
# also can write like this
friuts = ["apple", "banana", "cherry"]
for item in friuts:
    if item == "banana":
        continue
    print(item)

# understanding range function in for loop
print("\n")
for i in range(1, 6):
    print(i)
# increamenting the sequence with 2
print("\n")
for i in range(1, 6, 2):
    print(i)

# understanding else with for loop
print("\n")
friuts = ["apple", "banana", "cherry"]
for item in friuts:
    if item == "banana":
        break
    print(item)
else:
    print("YES")

# understanding nested for loop
print("\n")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# using pass statements when you have no any content for for loop
print("\n")
for x in [1, 2, 3]:
    pass
