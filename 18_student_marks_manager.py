students = {}

def add_student(name, marks):
    students[name] = marks

def show_all():
    print("\nStudent Marks:")
    for name, marks in students.items():
        print(f"{name}: {marks}")

def find_topper():
    if not students:
        print("No students added yet.")
        return
    topper = max(students, key=students.get)
    print(f"\nTopper is {topper} with {students[topper]} marks")

# sample usage
add_student("Radhika", 95)
add_student("Anu", 88)
add_student("Kiran", 76)

show_all()
find_topper()
