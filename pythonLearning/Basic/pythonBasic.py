print("hello world")

x = 5
print(x)
print(x + 1)
print('hello data world !!!!!!')
print('----------------------------------------')
print("shipra mishra")
s = "hello world"
print('0th index = ', s[0])
print('1th index = ', s[1])
print('2th index =', s[2])
print('3th index =', s[3])
print('4th index =', s[4])
print('5th index =', s[5])
print('6th index =', s[6])

print('----------------------------------------')
print('-1 th index=', s[-1])
print('-2 th index=', s[-2])
print('-5th index =', s[-5])
print('-6th index =', s[-6])
print('------------------------------------')
s1 = "hello"
s2 = "world"
print(s1 + "  " + s2)
s1 = "Shipra"
s2 = "Manish"
print(s1 + " " + s2)
print('--------------------------------------')
print("hello_" * 5)
print("shipra_" * 5)
print('---------------------------')
s = "Namaste World"
print(s[0:7])
print(s[8:13])
print(s[0:13])
print(s[-5:])
print(s[-13:])
print('----------------------------')
s = "coding world"
print(s.upper())
print(s.lower())
print('-----------------------')
name = "Shipra"
age = 30
married = True
print("my name is %s, my age is %s,and it is %s that "
      "I am married" % (name, age, married))
print(f"my name is {name},and my age is {age}")
print(f"my name is {name}, and it is {married} that I am married")
my_string = "Hello, World!"
print(my_string[7])

print(my_string.replace("H", "J"))
print(my_string.replace("l", "k"))

print("---------working with numbers--------")
x = 4
y = 2
print("Result of x/y =", x / y)
print("result of x*y =", x * y)
print("result of x+y =", x + y)
print("result of x-y = ", x - y)

print("--------data type---------")
a = 42
b = 32.30
c = "Hello"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("---------working with list------")
my_list = [1, 2, 3]
print("my_list = ", my_list)
print("first element =", my_list[0])
print("second element =", my_list[1])
print("third element =", my_list[2])
print("length of above list =", len(my_list))

print("------adding new element to list_____")
my_list_2 = ['one', 'two', 'three', 4, 5]
print(my_list_2)
print("My second list =", my_list_2)
my_list_2.append("six")  # this is operation

print(my_list_2)
print("Appended result List =", my_list_2)
my_list_2.append("seven")
print(my_list_2)
my_list_2.append("Delhi")
print(my_list_2)

list = [1, 2, 3, ['a', 'b', 'c'], 'India']
list.append("3.5")
print(list)
print("append float number", list)
list.append(["country,state"])
print("append string", list)

print("------extend list with another list------")
list2 = [1, 2, 3]
list2.extend([4, 5])
print("extend list", list2)
# difference between append and extend
# in append we can add only one element at the end of list
# in extend we can add multiple elements at the end of the list

list2.extend([6, 7, 8])
print("extend list ==", list2)

print("----Range-------")
range1 = range(10)
print(range1)

print("manually without for loop")
print(range1[0])
print(range1[1])
print(range1[2])
print(range1[3])
print(range1[4])
print(range1[5])
print(range1[6])
print(range1[7])
print(range1[8])
print(range1[9])

# now print each element within the range
# loop / iteration / repeat and execute
# range1 = range(10)
print("manually with for loop")
for r in range1:
    print(r)

# Need to check this
# p = list(range(10))
# print(p)
# program to find odd even member in list
mixed_list = [10, 13, 11, 17, 14, 18, 20]


def filter_odd_even(num_list):
    even = []
    odd = []

    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even list is : {even}")
    print(f"Odd list is : {odd}")


print(f"Mixed list is : {mixed_list} ")
filter_odd_even(mixed_list)
