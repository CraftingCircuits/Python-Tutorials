# defining a function in a module
def greeting(name):
    print("Hello" + " " + name)


# defining variables in a module
# for list
my_list = [1, 2, 3, 4, 5, 6]
# for set
my_set = {1, 2, 3, 4, 5, 6}
# for tuple
my_tuple = (1, 2, 3, 4, 5, 6)
# for dictionary
my_dict = {"Name": "Niyati", "Age": 20, "City": "Mumbai", "Born": 2006}
# for a string
my_string = "Niyati is a good Painter and a good writer."
# for a number
my_number = 9824
# for a boolean
my_boolean = True


# defining a complex function to just understand how it works
def my_fun(a, b, c, d, e):
    if a >= b and a >= c and a >= d and a >= e:
        return "a is greatest"
    elif b >= a and b >= c and b >= d and b >= e:
        return "b is greatest"
    elif c >= a and c >= b and c >= d and c >= e:
        return "c is greatest"
    elif d >= a and d >= b and d >= c and d >= e:
        return "d is greatest"
    else:
        return "e is greatest"


# defining a function to determine sorted numbers
def sorted_numbers(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    numbers.sort()
    return numbers


# defining a function to determine the largest number
def largest_numbers(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    largest = max(numbers)
    return largest
