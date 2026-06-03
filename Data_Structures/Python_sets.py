# Python Sets 
# A set is a collection which is unordered, unchangeable*, and unindexed.
myset = {"one","two","three"}
print(myset)
# set doesn't allow duplicate items 
myset = {"one","two","three","one"}
print(myset)
# The values True and 1 are considered the same value in sets, and are treated as duplicates:
myset = {"one","two","three","one",True,1,3}
print(myset)
# The values False and 0 are considered the same value in sets, and are treated as duplicates:
myset = {"one","two","three","one",False,0,3}
print(myset)
# length of a set
myset = {"one","two","three","one",False,0,3}
print(len(myset))
myset = {"one","two","three"}
print(len(myset))
# type of a set
myset = {"one","two","three"}
print(type(myset))

# set can be any kind of data type
set1 = {"one","two","three"}
set2 = {1,2,3}
set3 = {True, False, True}
set4 = {"one",2,True}
print(set1)
print(set2)
print(set3)
print(set4)

# using set constructor
myset = set(("apple", "banana", "cherry")) 
print(myset)

# accessing items from a set using for loop
print("\n")
print("accessing items from a set using for loop")
myset = {"one","two","three"}
for item in myset:
    print(item)
    
# checking items in a set
myset = {"one","two","three"}
print("two" in myset)
print("two" not in myset)

# in a set, wwe can't change items in a set, but we can add items using add() method
print("\n")
print("adding items in a set")
myset = {"one","two","three"}
myset.add("four")
print(myset)

# adding a set to another set using update() method
print("\n")
print("adding a set to another set using update()")
myset = {"one","two","three"}
newset = {"four","five","six"}
myset.update(newset)
print(myset)

# adding a list to a set
print("\n")
print("adding a list to a set")
myset = {"one","two","three"}
mylist = ["four","five","six"]
myset.update(mylist)
print(myset)

# removing items from a set using remove method
print("\n")
print("removing items from a set")
myset = {"one","two","three"}
myset.remove("two")
print(myset)
# removing items from a set using discard method
print("\n")
print("removing items from a set")
myset = {"one","two","three"}
myset.discard("two")
print(myset)

# removing items from a set using pop method, pop() removes random item from a set
print("\n")
print("removing items from a set")
myset = {"one","two","three"}
x = myset.pop()
print(x)
print(myset)

# deleting a whole set using clear method
print("\n")
print("deleting a whole set")
myset = {"one","two","three"}
myset.clear()
print(myset)
# deleting a whole set using del operator
print("\n")
print("removing items from a set")
myset = {"one","two","three"}
del myset

# Python set Loop
# loopoing a set using for loop
print("\n")
print("looping a set using for loop")
myset = {"one","two","three"}
for item in myset:
    print(item)
    
# Python join sets
# joining two sets using union method, that joinw qll itemsfrom both sets
print("\n")
print("joining two sets using union method")
set1 = {"one","two","three"}
set2 = {"four","five","six"}
set3 = set1.union(set2)
print(set3)

# joining two sets using | operator, that joinw qll itemsfrom both sets
print("\n")
print("joining two sets using | operator")
set1 = {"one","two","three"}
set2 = {"four","five","six"}
set3 = set1 | set2
print(set3)

# joining multiple items in a set using union method
print("\n")
print("joining two sets using union method")
set1 = {"one","two","three"}
set2 = {"four","five","six"}
set3 = {1,2,3,4}
set4 = {"a","b","c","d"}
set5 = set1.union(set2,set3,set4)
print(set5)

# joining two sets using | operator, that joinw qll itemsfrom both sets
print("\n")
print("joining two sets using | operator")
set1 = {"one","two","three"}
set2 = {"four","five","six"}
set3 = {1,2,3,4}
set4 = {"a","b","c","d"}
set5 = set1 | set2 | set3 | set4
print(set5)

# joining a set with a tuple
# The union() method allows you to join a set with other data types,
x = {"a","b","c","d"}
y = (1,2,3,4)
z = x.union(y)
print(z)

# adding items in a set using update method
print("\n")
print("joining two sets using update method")
set1 = {"one","two","three"}
set2 = {1,2,3,4}
set1.update(set2)
print(set1)

# checking duplicate items in a set
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# this will create a new set
print("\n")
print("checking sets using intersection method")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set3 = set1.intersection(set2)
print(set3)
# checking duplicate items in a set using & operator
# this will create a new set 
print("\n")
print("checking sets using & operator")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set3 = set1 & set2
print(set3)
# checking duplicate items in a set using intersection_update() method
# this will change a original set
print("\n")
print("checking sets using intersection_update() method")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set1.intersection_update(set2)
print(set1)

# understanding same items and if it is considered as duplicate ones
print("\n")
print("understanding items in a set, if it is same or duplicate")
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# cheking different items in a set using diffrence method
# this will basically pe=rints items that are not present in other set
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
print("\n")
print("checking sets using difference() method")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set3 = set1.difference(set2)
print(set3)
# using - operator instead of difference method
print("\n")
print("checking sets using - operator")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set3 = set1 - set2
print(set3)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
print("\n")
print("checking sets using symmetric_difference method")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set3 = set1.symmetric_difference(set2)
print(set3)
# using ^ operator instead of symmetric_difference method
print("\n")
print("checking sets using ^ operator")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set3 = set1 ^ set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
# basically it will not returns a new set, it will change a set and returns it as output
print("\n")
print("understanding symmetric_diffrence_update() method to print diff items from both sets")
set1 = {"one","two","three"}
set2 = {"three","four","five"}
set1.symmetric_difference_update(set2)
print(set1)




