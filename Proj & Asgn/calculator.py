# Basic Calculator
# print("Welcome to the Basic Calculator.")
 
def operation(x,y,op):
    if  op == 'sumation':
        return x+y
    elif  op == 'subtraction':
        return x-y
    elif  op == 'multiplication':
        return x*y
    elif op == 'division':
         if y != 0:
            return x / y
         else:
            return "Error: Division by zero!" 
    else:
        return "Invalid Operation"

print("Welcome to the Basic Calculator.")

while True:
    user_input = input("\nType 'stop' or 'exit' to quit.\nEnter operation (sumation, subtraction, multiplication, division): ").strip().lower()
    if user_input in ['stop', 'exit']:
        print("Thanks for using the Basic Calculator. Goodbye!")
        break
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", operation(x,y,user_input))
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")
  
#   op = input("Enter operation(sumation, subtraction, multiplication, division):").strip().lower()
#   print("Result:", operation(x,y,op))