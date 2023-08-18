# conditional statement

a = 4
b = 6
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

print("result of a > b = ",(a>b))

print("result of b > a = ",(b>a))
c = 2
d = 2
if c > d:
    print("c is greater than d")
elif d > c:
    print("d is greater than c")
else:
    print("c and d are equal")

print("_____________________loop_______________________")

# loop means iterate (repetition of logic and work)
# a for loop acts as an iterator in python.
# we can use loop in different python collection/ data structure
# such as list,string,tuples
# iterator is going one by one to every element.

print("printing hello 5 times without using for loop")

print("hello")
print("hello")
print("hello")
print("hello")
print("hello")

# Loop using for
print("printing hello 5 times using for loop")
for i in range(5):
    print("hello")

print("One more way ")

print("hello" "    "* 5)

print("One more way ")

print("hello\n"* 5) # \n means new line

print("One more way ")

print("hello\t"* 5) # \t means new space

users = list(range(10))
print(users)

for i in range(10):
    print(i)

list_1 = [2,3,4,5,6,7,8,9,10]
# select one element in the list (even number)
for number in list_1:
    if number % 2 == 0:
        print("even numbers are", {number})
    else:
        print("odd numbers are",{number})

# while loops -
# differenece between for loop and while loop
# for loop works on the basis of number of iterator (means total number of element)
#but in the case of while loop , it will loop based on  the condition you will provide
# while statement will repeatedly execute a single statement or group of statement as long as the condition is true.

x = 0
while x < 10:
       print('x is currently: ',x,end =' ')
       print('x is still less than 10, adding 1 to x')
       x = x + 1




