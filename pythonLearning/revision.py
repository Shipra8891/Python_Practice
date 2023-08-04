# python string - strings are number of characters,
# such as letters,numbers,or symbols enclosed with quotes.


my_string = ("my name is shipra")
print(type(my_string))
print(my_string)

# extracting individual character
print(my_string[0])
print(my_string[-2])

# slicing
print(my_string[0:])
print(my_string[0:17:2])

# string function
print(len(my_string))
print(my_string.lower())
print(my_string.upper())
print(my_string.replace('a','u'))
print(my_string.count("i"))
print(my_string.find("is"))
print(my_string.split(" "))

# data structure in python - tuple,list,dictionary,set
# Tuples is an ordered collection of elements enclosed in ()
# (getting individual elements)
tuple = ('a','b','c','d','e','f')
print(tuple[0])
print(tuple[3])
print(tuple[5])
print(tuple[-4])
print(tuple[1:])
print(tuple[1:4])
print(tuple[0:5:2])

# tuple[0] = 'w' , tuple does not support assignment

# tuple basic operation (length)
print(len(tuple))

# concatenating tuples (add two variables)
tuple = ('a','b','c','d','e','f')
tuple1 =('g','h','i')
print(tuple + tuple1)

# min and max value of tuple
print(min(tuple))
print(max(tuple))

# List is an ordered collection of elements enclosed in []
list = ['a','1','b','2','c','3']

# (getting individual elements)
print(list[-3])
print(list[3])
print(list[1:5])
print(list[0:6])
print(list[1:5])

# list basic operation
# Changing the element at 0th index
(list[0])=100
print(list)

# Popping the last element
list.pop()
print(list)

# Appending a new element
list.append("hi team")
print(list)

# Concatenating lists
list1 =["22","44"]
print(list + list1)

# Reverse elements of a list
list.reverse()
print(list)

# Inserting element at specified index
list.insert(2,"gm")
print(list)

# Sorting a list
list1 = ["banana","apple","cherry"]
list1.sort()
print(list1)

# Dictionary is an unordered collection of key-value pairs
# enclosed in {}
# key and values in dictionary

# Extracting keys from a Dictionary
my_dict = {"name":"sonu","age":"30","city":"delhi"}
print(my_dict.keys())
print(my_dict.values())

# Modifying a Dictionary
# Adding a new element
my_dict["occupation"]= "CA"
print(my_dict)

# Changing an existing element
my_dict["age"]="32"
print(my_dict)

# Set is collection of unique elements with no duplicates
# enclosed in {}
my_set={1,3,2.5,"monday",3.5}
print(my_set)
my_set.add("hello")
print(my_set)
my_set.remove(3)
print(my_set)
# Updating multiple elements
my_set.update([10,"sunday","wednesday",25,15])
print(my_set)

# Set Function
s1={'a','b','c'}
s2={1,2,3}
#s1.union(s2)
print(s1.union(s2))

# Intersections of 2 Set
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.intersection(set2))

set3={1,1,2,2,4,3,5,5,}
print(set3)

# for reverse
a = ("shipra")


