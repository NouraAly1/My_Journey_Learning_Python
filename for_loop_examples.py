# For Loop Learning Examples
# This file contains different examples of how to use for loops in Python

# Example 1: Loop through each letter in a string
for letter in "noura":
    print(letter) Example 2: Loop through a list of names
kids = ["adam", "lily","amalia"]
print(len(kids))
for kid in kids:
    print(kid)

# Example 3: Loop through list indices instead of values
for kid in range(len(kids)):
    print(kid)

# Example 4: Loop through string indices
name = "noura"
for y in range(len(name)):
    print(y)

# Example 5: Use index to access list elements
for kid in range(len(kids)):
    print(kids[kid])

# Example 6: Check if numbers are even or odd
for number in range(6):
    if number % 2 ==0:
        print(number, "is even")
    else:
        print(number, "is odd")

# Example 7: Search for a specific item in a list
language = ["python", "css", "java", "html"]
for l in range(len(language)):
    if language[l] == "python":
        print(l, "is the right language")
    else:
        print(l, "is not the right language")

# Example 8: Skip a number using continue
for n in range(5, 10):
    if n == 8:
        continue
    print(n, "is the choosen number")