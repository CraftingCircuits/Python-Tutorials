# Python iterators and iterables
# example of an iterable object
# Return an iterator from a tuple, and print each value:
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# # return an iterator from a string, and print each value:
print("\n")
my_string = "Hello World"
my_iter = iter(my_string)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# # looping through an iterator, using a for loop:
print("\n")  # for a list, tuple, or dictionary
list = [1, 2, 3, 4, 5]
for item in list:
    print(item)
print("\n")  # for a string
string = "Hello World"
for char in string:
    print(char)

# creating an iterator using a class
print("\n")


# Stop Iteration is raised when there are no more items to return.
class Myiterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# # printing values from the iterator
# class MyNumbers:
#     def __init__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myClass = MyNumbers()
# myIter = iter(myClass)


# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
