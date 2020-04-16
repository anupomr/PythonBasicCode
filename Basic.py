# For loop
for item in "Canada":
    print(item.upper())

for item in ["Canada", "USA", "UK"]:  # List
    print(item.upper())

for item in range(1, 10, 2):  # 1 = starter (opt), 10 = range (req), 2 = step (opt)
    print(item)

# Add item in loop
price = [10, 20, 30]
total = 0
for item in price:
    total += item
print(f" Total price ${total}")
