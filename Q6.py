# Example showing that lists are mutable:

# Create a list:
fruits = ["apple", "banana", "cherry"]

# Modify the second element
fruits[1] = "blueberry"

print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Example showing that strings are not mutable:

# Create a string:
word = "hello"

# Try to change the first letter (This will cause an error)
#word[0] = "H"  #TypeError: 'str' object does not support item assignment

# Instead, we would need to create a new string:

word = "H" + word[1:]  # Creating a new string
print(word)  # Output: "Hello"