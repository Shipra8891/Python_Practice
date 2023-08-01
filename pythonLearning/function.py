# modular programming in python
# function
# reuse code - there are many cases where we need to use same logic again and again.
# so instead of writing same code again and again we can write a function
# and call the same function when needed.
# function contain group of statement and logic of the use case.
# example of inbuilt / predefined function.  len,lower,upper
# best practices to follow while code writing

# function without argument
def say_my_name():
    print("shipra")


say_my_name()


# function with argument
def double_the_number(num=1):
    return num * 2


print(double_the_number())  # default argument
print(double_the_number(4))  # passing argument


# positional argument
def double_the_number1(num):
    return num * 2


print(double_the_number1(8))  # default argument
print(double_the_number1(7))  # passing argument


def add_the_number1(a1, a2):
    return a1 + a2


print("result of addition", add_the_number1(10, 22))


# def name_of_fucntion( number of argument ) :
# return
def database_columns(*args):
    for arg in args:
        print(arg)


print(database_columns("name", "age"))

# lambda function - this is just like function
# but we do not use def key word to define this,
# also it doesnot have any name.
# we directly write lambda and the logic of work

square_data = lambda num: num ** 2  # (** - means power of )
print(square_data(4))

add_data = lambda num1, num2: num1 + num2
print(add_data(10, 20))

cal_data = lambda p1, p2, p3: ((p1 + p2) - p3)
print(cal_data(10,20,30))

cal_data1 = lambda q1, q2, q3: (q1 * q2 / q3)
print(cal_data1(10,20,10))


