# object-oriented programming
# every thing inside python is object  means what ever you create list , tuple , variable is object
# you can use functions in your object to do work
# create a new object type called sample

s = "my name is shipra"
print(type(s))

s.lower()
s.upper()

# object
print(type(1))
print(type([]))
print(type(()))
print(type({}))


# how we can create our own object in python
# we can do this by using keyword class
class Sample():
    pass


# create instance of class
x = Sample()
print(type(x))

print("--------------------------")

x = 5


def add(a, b):
    c = a + b
    return c


print(add(2, 3))

print(add(33,44))


class Teacher:
    # A simple class  # attribute
    role1 = "Principal"
    role2 = "Co-coordinator"

    # A sample method
    def fun(self):
        print("My role is ", self.role1)
        print("My role is ", self.role2)


# Driver code
# Object instantiation
School = Teacher()

# Accessing class attributes
# and method through objects
print("My School Detail", School.role1)
School.fun()


# class can contain varibale and function both in it.
# we can instantiate the class and call variable and function as per requiremnt

class Rectangle:
    length = 2
    breadth = 3

    def area(self):
        a = self.length * self.breadth
        return a


MathArea = Rectangle()
# MathArea is object of this class or class instance

print("Length of rectangle =", MathArea.length)
print("Breadth of rectangle =", MathArea.breadth)
print("Area of rectangle", MathArea.area())


# The __init__() Function

# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object argument
# when ever class is initiated __init__ function will be called automatically and it will set the parameter value
class Person:
    def __init__(self, name, age):
        self.name = name  # self.name is not variable here ...in class we call it attribute
        self.age = age


p1 = Person("Manish", 36)  # class initiation or instance creation or object creation
p2 = Person("Shipra", 30)
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p1)
print(p2)
# P1 is instance for Manish and P2 is instance for Shipra
# P1 is not equal to p2
print(p1 == p2)


# area of circle

class Circle:
    pi = 3.14  # it will common for every instance # class level variable or attribute

    def __init__(self, radius):  # constructor
        self.radius = radius

    def area(self):
        # return self.radius * self.radius * 3.14
        return self.radius * self.radius * Circle.pi


print("Class for area of circle")
c1 = Circle(3)  # initiate / instantiate / create object
print(c1)
c1.area()
print("Area of circle =", c1.area())

c2 = Circle(7)
c2.area()

# Practice school name example of darshil

# difference between class level attribute and instance level attribute
# Class level attribute is same for every instance
# instance level attribute is different for every instance

# practice .show from student class of darshil

