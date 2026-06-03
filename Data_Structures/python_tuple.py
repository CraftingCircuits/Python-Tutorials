# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
mytuple = ("one","two","three")
print(mytuple)

# tuple items are indexed, it means the first item has index[0] the second items has index[1]
# tuples are ordered it means the items have defined order, that will not change
# tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# tuples allows duplicates
mytuple = ("one","two","three","one","four")
print(mytuple)

# tuple length 
print("\n")
print("length of the tuple")
mytuple = ("one","two","three","one","four")
print(len(mytuple))

# creating tuple with one item, have to add come after item
print("\n")
print("It is a tuple with one item")
mytuple = ("one",)
print(mytuple)
print("It is not a tuple")
mytuple = ("one")
print(mytuple)

# tuple can contain items of any kind of data type
print("\n")
print("tuple can contain all data type")
tuple1 = ("one","two","three","four")
tuple2 = (12,23,34,45)
tuple3 = (True,False,True)
tuple4 = ("one",34,"two",True)
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

# tuple constructor
print("\n")
print("understanding a tuple constructor")
mytuple = tuple(("apple","banana","cherry"))
print(mytuple)

# access tuples using index
print("\n")
print("understanding indexing in tuple")
mytuple = ("one","two","three","four","five")
print(mytuple[3])
print(mytuple[-2])
print(mytuple[2:5])
print(mytuple[-3:-1])
print(mytuple[1:2])

# check if item exist in tuple
print("\n")
print("founding items in a tuple")
mytuple = ("one","two","three","one","four")
if "one" in mytuple:
    print("Yes it is exist")
    
# can't change tuple's items, but can convert tuple into list
print("\n")
print("adding items in a tuple by converting it into a list")
x = ("one","two","three","one","four")
y = list(x)
y[1] = "six"
x = tuple(y)
print(x)

# converting into list, add item and then converting it into tuple again
print("\n")
print("adding items in a tuple using append method")
x = ("one","two","three","one","four")
y = list(x)
y.append("six")
x = tuple(y)
print(x)

# adding tuple to a tuple
print("\n")
print("adding a tuple into another tuple")
x = ("one","two","three","one","four")
y = ("six",)
x += y
print(x)

# to remove items from tuple, convert it into list, remove and then convert it into tuple again
print("\n")
print("removing items from a tuple using remove method")
x = ("one","two","three","one","four")
y = list(x)
y.remove("two")
x = tuple(y)
print(x)

# to delete a tuple completely, remove all items
print("\n")
print("deleting whole tuple using del")
mytuple = ("one","two","three","one","four")
del mytuple

# unpacking a tuple
print("\n")
print("unpacking a tuple\n")
mytuple = ("one","two","three","four","five")
(one,two,three,four,five) = mytuple
print(one)
print(two)
print(three)

# using asterisk to unpacking a tuple
print("\n")
print("unpacking a tuple using asterisk")
mytuple = ("one","two","three","four","five","six","seven")
(one,two,three,*num) = mytuple
print(one)
print(three)
print(num)

# assigning a asterisk at other index
print("\n")
mytuple = ("one","two","three","four","five","six","seven")
(one,two,*num,num1,num2) = mytuple
print(one)
print(*num)
print(num2)

# looping a tuple using for
print("\n")
print("looping a tuple using for loop")
mytuple = ("one","two","three","four","five","six","seven")
for item in mytuple:
    print(item)
    
# looping using index numbers
print("\n")
print("looping through indexing")
mytuple = ("one","two","three","four","five","six","seven")
for i in range(len(mytuple)):
    print(mytuple[i])

# looping using while loop
print("\n")
print("looping through while loop")
mytuple = ("one","two","three","four","five","six","seven")
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i=i+1
    
# joining two tuples
print("\n")
print("joining two tuples using plus operator")
tuple1 = ("one","two","three")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiplying two tuples
print("\n")
print("multiplying two tuples using asterisk operator")
tuple1 = ("one","two","three")
tuple3 = tuple1*2
print(tuple3)

# tuple methods
print("\n")
print("Using bothe tuple methods")
tuple1 = ("one","two","three")
print(tuple1.count("one"))
print(tuple1.index("one"))


