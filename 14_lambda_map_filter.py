lambda = small anonymous function
square = lambda x: x * x
print(square(5))

nums = [1, 2, 3, 4, 5]

# map: apply function to each element
squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)

# filter: keep only elements that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)
