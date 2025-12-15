15_my_math.py:

def add(a, b):
    return a + b

def sub(a, b):
    return a - b
15_use_my_math.py:

import 15_my_math as mm  # if name starts with number, change to my_math.py instead!

print(mm.add(10, 5))
print(mm.sub(10, 5))

