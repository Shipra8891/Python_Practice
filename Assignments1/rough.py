#
import d

a = [10,20,30,20,10,50,60,40,80,50,40]
(set(a))
print(set(a))
print("_______________sum___________________")
b = [1,2,-8]
sum(b)
print(sum(b))

c = ['abc', 'xyz', 'aba', '1221']
print("--------------------------------------")
output = [x for x in c if len(x) >= 2 and x[0] == x[-1]]
print("Output is ",output)
print("length of output element",len(output[0]),len(output[1]))
print("------------------------------------------")
for x in c:
    if len(c) >= 2 and x[0] ==x[-1]:
       print(x)

print("-------------remove index---------------")
list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
output =list1[1:4]
print(output)

print("-------------removing even number--------------")
list2 = [7,8,120,25,44,20,27]
list2 = [x for x in list2 if x%2 == 1]
print(list2)

print("____________________________________")
list_1= [10,20,30,40,20,50,60,40]
set(list_1)
print(set(list_1))

print("-------------------------------------")
list_2 = ['a','b','c','d']
print(''.join(list_2))

print("______________uncommon elements________________________")
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]
print(set(list1)^set(list2))

print("------------to check frequency--------------------------")
a = [1, 2, 3, 2, 4, 1, 3, 5, 2, 3, 4, 1]
output_a = {x: a.count(x) for x in set(a)}
print(output_a)

print("-----------to find common items-----------")
color1 = ("Red","Green","Orange","White")
color2 = ("Black","Green","White","Pink")
common_items = set(color1) & set(color2)

print("common element")
print(common_items)

print("___________concatenate list with range______________")
given_list= ['p','q']
n = 5
output_list = [item + str(i) for i in range(1,n+1)for item in given_list]
print(output_list)

print("------conversion of multiple list into single integers___________")
multiple_list= [11,33,50]
single_list= (''.join(str(num) for num in multiple_list))
print(single_list)

print("__________________split__________________")
list_3= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
n = 3
split_output= [list_3[i::n] for i in range(n)]
print(split_output)

print("__________Tuple___________")
input=(4,8,3)
print("A1=",input[0])
print("A2=",input[1])
print("A3=",input[2])

tuple_1 =(4,8,3)
A1,A2,A3= tuple_1
print("A1=",A1)
print("A2=",A2)
print("A3=",A3)

print("______________to check element exist___________________")
tuple_2= ("w",3,"r","e","s","o","u","r","c","e")
element_exist= 5 in tuple_2
print(element_exist)

print("______________reverse________________")
tuple_3=(5,10,15,20)
reverse= tuple_3[-1::-1]
print(reverse)


print("_________string formatting_________________")
input = (100,200,300)
print("This is a tuple",(100,200,300))

print("-----------remove empty tuple______________")
tuple_list = [(), (), ('a','b'), ('a','b','c'), 'd']
output_list= [t for t in tuple_list if t]
print(output_list)

print("-------------convert a string to tuple--------------")
string=('s','h','i','p','r','a')
tuple_result =(tuple(string))
print(tuple_result)

print("__________sum of tuple__________")
tup1 =(1,2,3,4)
tup2 =(3,5,2,1)
tup3 =(2,2,3,1)

tup_res = tuple(map(sum,zip(tup1,tup2,tup3)))
# what is map ??????
print(tup_res)

print("___convert list of tuple into list of list____________")
input_list = [(1,2),(2,3),(3,4)]
tupleto_list = [list(t) for t in input_list]
print(tupleto_list)

print("___________SET_____________")
S1 = {1,2,3,4}
S2 = {4,5,6,7}
print("False,common element is",(S1 & S2))

print(S1.isdisjoint(S2))

print("-----------check element exist or not-------------------------")
set_1 = {1,3,5,7,9,11}

for i in set_1:
        if i==10:
            print("true")
        else:
            print("False")
print("______another method________")
value_to_check = 10
print(value_to_check in set_1)

print("-------remove duplicates________")
data_set= ["Python","Exercise","Practice","Solution","Exercise"]
print(set(data_set))

print("---------dictionary--------------")
print("add new value")
dict = {0:10,1:20}
new_key=2
new_value=30
dict[new_key]=new_value
print(dict)

dict[2]=30
print(dict)



print("------concatenate dictionary----------")
dic1={0:10,1:20}
dic2={3:30,4:40}
dic3={5:50,6:60}

output_dict={}
output_dict.update(dic1)
output_dict.update(dic2)
output_dict.update(dic3)
print(output_dict)

print("______remove a key__________")
input_dictionary = {
           'name':'John Doe',
           'age': 30,
           'occupation':'Software Engineer',
           'email':'john@example.com',
           'is_employed':True
                   }
key_to_remove= 'age'
del input_dictionary[key_to_remove]
print(input_dictionary)

print("__________remove duplicates_____________")
original_dict = {'a':1,'b':2,'c':3,'d':3,'e':2,'f':4}
temp=[]
resultant_dictionary ={}
for key ,val in original_dict.items():
    if val not in temp:
        temp.append(val)
        resultant_dictionary[key] = val

print(resultant_dictionary)

print("-------find max and min values of a dictionary--------")
# find max and min value of a dictionary
# Input: {‘u’:1000,’v’:3000,'x':500, 'y':5874, 'z': 560}
# use max() and min() functions to find values

dictionary = {'u':1000,'v':3000,'x':500,'y':5874,'z':560}

max_value= max(dictionary.values())
print("Maximum Value :",max_value)

min_value= min(dictionary.values())
print("Minimum Value :",min_value)

# How to check if dictionary is empty
# Use the if statement to check if the dictionary is empty.
# input : my_dict = {}

my_dic = {}

if not my_dic :
    print("Dictionary is Empty")
else:
    print("Dictionary is not Empty")

# find fifth value of each key from dictionary.
# input:
input_dict ={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
            'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
            'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

value_x =input_dict['x'][4]
value_y =input_dict['y'][4]
value_z =input_dict['z'][4]

print(value_x)
print(value_y)
print(value_z)

# drop empty (None value) items from dictionary
# Input: {'c1': 'Red', 'c2': 'Green', 'c3': None}

input_dict = {'c':'Red','c2':'Green','c3':None}
output_dict ={key:value for key,value in input_dict.items() if value is not None}

print(output_dict)

# filter out from dictionary.
# find the values > 170 from dictionary.

Input_dict: {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox':190}
output_dict1 ={key:value for key,value in Input_dict.items() if value > 170}
print(output_dict1)

# how to verify that all values in a dictionary are same.
# Input: {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# use set() to check if it has only one element

input_dictionary = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
if len(set(input_dictionary.values()))==1:
    print("All values are",list(set(input_dictionary.values()))[0])
else:
    print("Values are not the same")

# convert dictionary into integer type.
# INPUT:[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}
convert_dict= [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
integer_dict =[{key:int(value) for key,value in d.items() for d in convert_dict}]




