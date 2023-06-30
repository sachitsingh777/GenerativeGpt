# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

# Input list of tuples
data = [("John", 25), ("Jane", 30)]

# Iterate through the list and unpack each tuple
for name, age in data:
    print(f"{name} is {age} years old.")





# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]


# Creating an empty dictionary
person_dict = {}

# Adding name-age pairs
add_person(person_dict, "John", 25)
add_person(person_dict, "Jane", 30)

print(person_dict)  # Output: {'John': 25, 'Jane': 30}

# Updating age
update_age(person_dict, "John", 26)
print(person_dict)  # Output: {'John': 26, 'Jane': 30}

# Deleting a person
delete_person(person_dict, "John")
print(person_dict)  # Output: {'Jane': 30}



  
# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def two_sum(nums, target):
    complement_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i

    return []


# Test case
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]




# 4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    # Convert the word to lowercase and remove whitespace
    word = word.lower().replace(" ", "")
    
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False

# Test the function
word = "madam"
result = is_palindrome(word)
if result:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")





# 5. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the function
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)

  
# 6. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from queue import Queue

class Stack:
    def __init__(self):
        self.q = Queue()
    
    def push(self, item):
        # Add the item to the queue
        self.q.put(item)
    
    def pop(self):
        # Check if the stack is empty
        if self.is_empty():
            return None
        
        # Remove and return the topmost item from the stack
        size = self.q.qsize()
        
        # Remove and add all items except the last one to a temporary queue
        for _ in range(size - 1):
            self.q.put(self.q.get())
        
        # Remove and return the last item (topmost item)
        return self.q.get()
    
    def is_empty(self):
        # Check if the stack is empty
        return self.q.empty()

# Test the stack implementation
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None


# 7. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Zip the lists together and reverse list2
zipped_lists = zip(list1, reversed(list2))

# Iterate through the zipped lists and print the items
for item1, item2 in zipped_lists:
    print(item1, item2)



# 8. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Initialize the dictionary with default values
new_dict = {name: defaults for name in employees}

print(new_dict)



  
# 9. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

# Create a new dictionary by extracting specific keys
new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)
