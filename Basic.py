# For loop
for item in "Canada":
    print(item.upper())

for item in ["Canada", "USA", "UK"]:  # List
    print(item.upper())

for item in range(1, 10, 2):  # 1 = starter (opt), 10 = range (req), 2 = step (opt)
    print(item)

# Add item in loop
price = [10, 20, 30]  # imaginary shopping cart
total = 0
for item in price:
    total += item
print(f" Total price ${total}")

# Nested loop
numbers = [5, 2, 5, 2, 2]  # to display big F
for x in numbers:
    display = ""
    for item in range(x):
        display += "X"
    print(display)

# Nested loop to display big L
numbers = [2, 2, 2, 2, 10]  # to display big L
for x in numbers:
    display = ""
    for item in range(x):
        display += "X"
    print(display)

#  Write a program to find the largest number from a list
numbers = [2, 2, 2, 2, 10]
large = 0
numbers.insert(0, 22)
numbers.remove(2)
numbers.sort()
uniques = []
for number in numbers:  # To make the list unique
    if number not in uniques:
        uniques.append(number)

for number in numbers:  # to find the largest number from a list
    if number > large:
        large = number
print(large)
print(numbers)

# 2 Dimensional Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
matrix[0][2] = 21
print(matrix[0][2])
for row in matrix:
    print(row)

# Tuples structure
numbers = (11, 2, 3)  # This kind of list can't be change / mutable
print(numbers[0])

# Unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)
