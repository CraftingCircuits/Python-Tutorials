# Python lists
mylist = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
print(mylist)
# length of the list
print(len(mylist))
# type of the list
print(type(mylist))
# accessing items from the list
print(mylist[0])
print(mylist[2])
print(mylist[-1])
print(mylist[1:5])
print(mylist[1:3:2])
print(mylist[::-1])
print(mylist[3:-1:-1])
print(mylist[:5:-2])
# checking is an item exists in the list
print("apple" in mylist)
print("banana" not in mylist)
# change items in the list
mylist[0] = "kiwi"
print(mylist)
# change a range of item values in the list
mylist[2:5] = ["watermelon", "papaya", "pineapple"]
print(mylist)
# insert an item at a specified index
mylist.insert(2, "grape")
print(mylist)
# append an item to the end of the list
mylist.append("blueberry")
print(mylist)
# extend the list with another list
mylist.extend(["peach", "plum"])
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)
# remove an item from the list
mylist.remove("kiwi")
print(mylist)
# remove an item at a specified index
mylist.pop(2)
print(mylist)
# remove the last item from the list
mylist.pop()
print(mylist)
# using del keyword to remove an item at a specified index
del mylist[1]
print(mylist)
# using del keyword to remove the entire list
del mylist
# clear the list
print("clearing the list")
mylist = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
mylist.clear()
print(mylist)

# loop through the list
print("looping through the list")
mylist = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
for item in mylist:
    print(item)
    
# loop through the list using range
print("loop through the list using range")
for i in range(len(mylist)):
    print(mylist[i])
    
# loop through the list using while loop
print("loop through the list using while loop")
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1
    
# loop through the list using enumerate
print("loop through the list using enumerate")
for index, item in enumerate(mylist):
    print(f"Index: {index}, Item: {item}")
    
# looping using list comprehension
print("looping using list comprehension")
mylist = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
newlist = [item for item in mylist if "a" in item]
print(newlist)

# syntax for list comprehension
# newlist = [expression for item in iterable if condition == True]
# checking the condition
print("checking the condition")
newlist = [item for item in mylist if item != "banana"]
print(newlist)

# understanding the iterable
print("understanding the iterable")
newlist = [item for item in range(10)]
print(newlist)
newlist = [item for item in range(10) if item < 5]
print(newlist)

# understanding the expression
print("understanding the expression")
newlist = [item.lower() for item in mylist]
print(newlist)

# set all values in the  new list to 'hello'
print("set all values in the new list to 'hello")
newlist = ["hello" for item in mylist]
print(newlist)

# sorting the list alphanumerically
print("sorting the list alphanumerically")
mylist = ["orange", "kiwi", "apple", "banana", "mango", "cherry"]
mylist.sort()
print(mylist)
mylist = [100, 94,87,84,93,30,2,59,34,93]
mylist.sort()
print(mylist)

# sorting the list descendingly
print("sorting the list descendingly")
mylist = ["orange", "kiwi", "apple", "banana", "mango", "cherry"]
mylist.sort(reverse = True)
print(mylist)
mylist = [100, 94,87,84,93,30,2,59,34,93]
mylist.sort(reverse = True)
print(mylist)

# customizing the sort ordered list
print("customizing the sort ordered list")
mylist = ["orange", "kiwi", "apple", "banana", "mango", "cherry","grape","watermelon", "poha", "pie"]
def myfun(item):
    return len(item)
mylist.sort(key = myfun)
print(mylist)
print("customizing the sort ordered list for numbers")
def myfun(n):
    return abs(n-50)
mylist = [176,34,46,24,67,95,37,59,93,496,825,58,93]
mylist.sort(key = myfun)
print(mylist)

# customizing the sort ordered list with case insensitive sorting
print("customizing the sort ordered list with case insensitive sorting")
mylist = ["orange", "kiwi", "apple", "banana", "mango", "cherry","grape","watermelon", "poha", "pie"]
mylist.sort()
print(mylist)
mylist.sort(key = str.lower)
print(mylist)

# reversing the order of the list
print("Reversing the order of the list")
mylist = ["orange", "kiwi", "apple", "banana", "mango", "cherry","grape","watermelon", "poha", "pie"]
mylist.reverse()
print(mylist)

# copying the one list to other one
print("copying the list")
newlist = ["cabage", "flower", "chili","capsicum"]
mylist = newlist.copy()
print(mylist)

# using list method to copy list
print("using list method")
newlist = ["cabage", "flower", "chili","capsicum"]
mylist = list(newlist)
print(mylist)

# using slice operator to copy list
print("using slice operator")
newlist = ["cabage", "flower", "chili","capsicum"]
mylist = newlist[:]
print(mylist)

# joining two list using + operator
print("joining two lists using plus operator")
list1 = ["a","b","c","d"]
list2 = ["A","B","C","D"]
list3 = list1 + list2 
print(list3)

# appending all elements from one list into another list
print("using append method")
list1 = ["a","b","c","d"]
list2 = ["A","B","C","D"]
for x in list2:
    list1.append(x)
print(list1)

# extending all elements from one list into another list
print("using extend method")
list1 = ["a","b","c","d"]
list2 = ["A","B","C","D"]
list1.extend(list2)
print(list1)