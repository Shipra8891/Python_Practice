# Comprehensions in Python are used to
# generate new sequences based on existing sequences.
# comprehension increases the coding speed
# and makes it easy tp read the code.

import math

# list comprehension
names = ["Ravi", "Puja", "Vijay", "Kiran"]
print(names)

for name in names:
    print(f"hello  {name}")


names = ["Ravi", "Puja", "Vijay", "Kiran"]
hello = ["hello " + name for name in names ]
print(hello)

numbers = [55, 32, 87, 99, 10, 54, 32]
even = [num for num in numbers if num % 2 == 0]
print(even)
odd = [num for num in numbers if num % 2 == 1]
print(odd)

# for math.pow - you need to import math library

p = math.pow(2,2)
print(p)
p1 = math.pow(2,3)
print(p1)

# exceptional handling
# try and except statement

try:
    x = 1/0
except ZeroDivisionError:
    print('divided by zero')
    print('executed when exception occurs')


