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

print("Length of rectangle =",MathArea.length)
print("Breadth of rectangle =",MathArea.breadth)
print("Area of rectangle",MathArea.area())






