# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"

print("Hello World")

# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."

# Integer
num_int = 10
print("Type of num_int:", type(num_int), "Value:", num_int)

# Float
num_float = 3.14
print("Type of num_float:", type(num_float), "Value:", num_float)

# String
str_var = "Hello, World!"
print("Type of str_var:", type(str_var), "Value:", str_var)

# Boolean
bool_var = True
print("Type of bool_var:", type(bool_var), "Value:", bool_var)

# List
list_var = [1, 2, 3, 4, 5]
print("Type of list_var:", type(list_var), "Value:", list_var)

# Tuple
tuple_var = (1, 2, 3, 4, 5)
print("Type of tuple_var:", type(tuple_var), "Value:", tuple_var)

# Dictionary
dict_var = {"name": "John", "age": 25}
print("Type of dict_var:", type(dict_var), "Value:", dict_var)

# Set
set_var = {1, 2, 3, 4, 5}
print("Type of set_var:", type(set_var), "Value:", set_var)




# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."
num_list = list(range(1, 11))

num_list.append(20)
num_list.remove(5)
num_list.append(5)
num_list.sort()
print(num_list)

# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"
numbers = [10, 20, 30, 40]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)

# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

original_string = "Python"
reversed_string = reverse_string(original_string)
print(reversed_string)

# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

input_string = "Hello"

vowel_count = 0
for char in input_string:
    if char.lower() in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)



# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."


def is_prime_number(num):
    import math

    if num > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
    else:
        print(num, "is not a prime number.")

# Test the function
is_prime_number(13)
is_prime_number(25)

# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)


# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"
n = 5
fib_sequence = []
fib_sequence = [0, 1]  # Initialize with the first two numbers
while len(fib_sequence) < n:
    next_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_num)
print(fib_sequence)




# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
numbers = range(1, 11)
squares = [num ** 2 for num in numbers]
print(squares)
