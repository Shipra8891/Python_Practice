list1 = [1,2,3]
print(list1*3)

list_1 = [2,4,5,6,8,7,9,10]
for number in list_1:          # Selects one element in list_1
    if number % 2 == 0:        # Checks if it is even. IF even, only then goes to next step else performs above step and continues iteration
        print(f"This is an even number {number}")  # prints no if even. end=' ' prints the nos on the same line with a space in between. Try deleting this command & seeing the difference.
    else:
        print(f"This is an odd number {number}")

num_str = ('10')
num_int = int(num_str)


# swap the values of two variables in python
a = 5
b = 10
a, b = b, a

print(a,b)