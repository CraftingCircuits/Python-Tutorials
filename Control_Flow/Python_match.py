# python match ststements
# syntax :
# match expression:
# case x:
#     code block
# case y:
#     code block
# case z:
#     code block

# understanding by an example
# print("Enter a number to see a day: ")
# day = int(input())
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")

# understanding default value in match using underscore '_'
# num = 7
# match num:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case 5:
#         print("Five")
#     case _:
#         print("number")

# understanding combine values in match statements, using pipe character | as an or operator
# num = 6
# match num:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Less than five")
#     case 6 | 7 | 8 | 9 | 10:
#         print("More than five")
#     case _:
#         print("no")

# unedrstanding if statements as guard in match statements
# num_sequense = 20
# num = 5
# match num:
#     case 1 | 2 | 3 | 4 | 5 if num_sequense % 2 == 0:
#         print("it's an even")
#     case 1 | 2 | 3 | 4 | 5 if num_sequense % 2 != 0:
#         print("it's an odd")
