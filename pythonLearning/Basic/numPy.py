# for installing - pip install numpy
# ndarray
# slice it to make python object

import numpy as np
# download the required dependency
print(np.array)

# create an array in python
list1 = [10,20,30]
print(np.array(list1))
print(type(np.array(list1)))
print(np.array(list1).shape)
print(np.array(list1).dtype)

list_of_lists = [[5,10,15],[20,25,30],[35,40,45]]
print(np.array(list_of_lists))

print(np.array(list_of_lists).shape)
print(np.array(list_of_lists).dtype)

# numPy built in function or methods

arrange =np.arange(0,10)
print(arrange)
print(np.arange(0,10,2))

# zeroes and ones array
print(np.zeros((2,3)))
print(np.ones((2,5)))

#linspace
print(np.linspace(0,10,7))

# generate random numbers

print(np.random.rand(3,4))


print(np.random.randint(4,40,10))











