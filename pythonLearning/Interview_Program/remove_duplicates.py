# Consider the list of strings
import numpy
import pandas

fruits = ["nuts", "fruits", "veg", "fruits", "veg", "eggs", "fruits", "veg", "eggs"]

# by using set()
print(list(set(fruits)))

# by using list comprehension
final = []
[final.append(i) for i in fruits if i not in final]
print(final)

# using for loop
final = []
for i in fruits:
    if i not in final:
        final.append(i)
    print(final)

# Using numpy.unique()
print(numpy.unique(fruits))

# Using pandas.unique()
print(pandas.unique(fruits))


a = 5
b = 10

(a,b) = (b,a)
print(a,b)