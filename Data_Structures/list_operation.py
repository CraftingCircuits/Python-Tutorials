# num = int(input("Enter numbers separated by space: "))

# print("Numbers in the list:", listed_numbers)
from math import factorial
import statistics
listed_numbers = list(map(int, input("Enter numbers separated by space: ").split()))
def list_operations(listed_numbers):
    if not listed_numbers:
        return "The list is empty."
    
    total = sum(listed_numbers)
    average = total / len(listed_numbers)
    maximum = max(listed_numbers)
    minimum = min(listed_numbers)
    sorted_numbers = sorted(listed_numbers)
    reversed_numbers = list(reversed(listed_numbers))
    unique_numbers = list(set(listed_numbers))
    count = len(listed_numbers)
    even_numbers = [num for num in listed_numbers if num % 2 == 0]
    odd_numbers = [num for num in listed_numbers if num % 2 != 0]
    positive_numbers = [num for num in listed_numbers if num > 0]
    negative_numbers = [num for num in listed_numbers if num < 0]
    square_numbers = [num ** 2 for num in listed_numbers]
    cube_numbers = [num ** 3 for num in listed_numbers]
    prime_numbers = [num for num in listed_numbers if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    palindrome_numbers = [num for num in listed_numbers if str(num) == str(num)[::-1]]
    factorial_numbers = [factorial(num) for num in listed_numbers if num >= 0]
    same_range_numbers = [num for num in listed_numbers if num >= 0 and num <= 100]
    standard_deviation = statistics.stdev(listed_numbers) if len(listed_numbers) > 1 else 0
    variance = statistics.variance(listed_numbers) if len(listed_numbers) > 1 else 0
    range_value = maximum - minimum
    median_value = statistics.median(listed_numbers)
    mode_value = statistics.mode(listed_numbers) if len(set(listed_numbers)) < len(listed_numbers) else None
    
    return {
        "total" : total,
        "average" : average,
        "maximum" : maximum,
        "minimum" : minimum,
        "sorted_numbers" : sorted_numbers,
        "reversed_numbers" : reversed_numbers,
        "unique_numbers" : unique_numbers,
        "count" : count,
        "even_numbers" : even_numbers,
        "odd_numbers" : odd_numbers,
        "positive_numbers" : positive_numbers,
        "negative_numbers" : negative_numbers,
        "square_numbers" : square_numbers,
        "cube_numbers" : cube_numbers,
        "prime_numbers" : prime_numbers,
        "palindrome_numbers" : palindrome_numbers,
        "factorial_numbers" : factorial_numbers,
        "same_range_numbers" : same_range_numbers,
        "standard_deviation" : standard_deviation,
        "variance" : variance,
        "range" : range_value,
        "median" : median_value,
        "mode" : mode_value,
        
    }
    
result = list_operations(listed_numbers)
print("List Operations: ")
for operation, value in result.items():
    print(f"{operation} : {value}")