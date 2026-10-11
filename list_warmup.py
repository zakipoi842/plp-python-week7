# Week 7 Assignment — Part A: List Warmup
# Demonstrates index access, .append(), .remove(), and len().

fruits = ["apple", "banana", "cherry", "mango"]

# First and last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add a fifth fruit with .append()
fruits.append("orange")
print("After append:", fruits)

# Remove one fruit with .remove()
fruits.remove("banana")
print("After remove:", fruits)

# How many remain
print("Number of fruits:", len(fruits))