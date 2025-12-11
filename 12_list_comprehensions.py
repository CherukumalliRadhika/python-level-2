numbers = [1, 2, 3, 4, 5]

# square of each number (normal loop)
squares_normal = []
for n in numbers:
    squares_normal.append(n**2)
print("Normal:", squares_normal)

# same using list comprehension
squares_comp = [n**2 for n in numbers]
print("Comprehension:", squares_comp)

# keep only even numbers
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)
