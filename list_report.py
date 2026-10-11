# Week 7 Assignment — Part C: List Report
# Prints a numbered list, counts items with more than 4 letters,
# and finds the longest item name — all using loops.

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Print each item numbered starting at 1
print("Numbered list:")
for i in range(len(items)):
    print(f"  {i + 1}. {items[i]}")

# 2. Count items with more than 4 letters
long_names = 0
for name in items:
    if len(name) > 4:
        long_names += 1
print(f"\nItems with more than 4 letters: {long_names}")

# 3. Find the longest item using a loop comparison
longest = items[0]
for name in items:
    if len(name) > len(longest):
        longest = name
print(f"Longest item name: {longest}")