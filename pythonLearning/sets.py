# collection of unique elements with no duplicates
sets1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, ]
print("result of sets1 =", set(sets1))
x = set()
x.add(1)
print(x)
x.add(2)
print(x)
x.add(3)
print(x)
x.add(1)
print(x)
# no repeats if add same elements in above sets
x.remove(2)
print("result after removing 2 =", (x))
x.remove(1)
print("result after removing 1 =", (x))
# create a list with repeats
sets2 = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
print("result of sets2 =", set(sets2))
# sets arrange in ascending order

print("-------------tuples___________________")
# tuples are ordered,unchangeable and allow duplicate values.
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[-1])
