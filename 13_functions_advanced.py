def greet(name="Guest"):
    print(f"Hello {name}")

greet("Radhika")
greet()  # uses default

def add_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(add_all(1, 2, 3, 4))

def show_student(**details):
    for key, value in details.items():
        print(key, ":", value)

show_student(name="Radhika", branch="CSE", year=3)
