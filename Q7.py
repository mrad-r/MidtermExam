# Continue by replacing the numbers greater than 80 with their corresponding negative value
# (90 will be replaced with -90).
#
# Also replace the number lower than 40 with the sum of their digits: 39 is replaced by 12.
#
# print the list at the end
#
# Use only what we have learned in class. Provide some explanation in the form of comments.

import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Modify the list based on given conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]  # Replace with negative value
    elif random_numbers[i] < 40:
        num = random_numbers[i]
        digit_sum = (num // 10) + (num % 10)  # Sum the digits
        random_numbers[i] = digit_sum  # Replace with sum of digits

# Print the modified list
print(random_numbers)

