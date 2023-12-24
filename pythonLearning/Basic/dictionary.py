
#dictionary: collection of unique value stored in (key-value) pairs
my_dictionary = {'key1': 'value1','key2':'value2'}
print(my_dictionary)
print(my_dictionary['key1'])
print("dictionary value is",my_dictionary['key1'])
print(my_dictionary['key2'])
my_dictionary['key1'] = 123
my_dictionary['key2'] = 456
print("value of key1 =",my_dictionary['key1'])
print("value of key2 =",my_dictionary['key2'])
my_dictionary1 ={'animals':'dog','birds':'crow'}
print(my_dictionary1)
my_new_dictionary = {'name': 'shipra','surname':'mishra'}
print(my_new_dictionary)
print("value of name key =",my_new_dictionary['name'])
print("value of surname key =",my_new_dictionary['surname'])
my_new_dictionary1 ={'name':["shipra","shubhra","riya"]}
print(my_new_dictionary1['name'])
print(my_new_dictionary1['name'][-1])
print(my_new_dictionary1['name'][0])
print(my_new_dictionary1['name'][1])
print(my_new_dictionary1['name'][2])
my_new_dictionary2 ={'name':["shipra","shubhra","riya"],'surname':["mishra","pathak","pandey"],'age':["26","27",28]}
print("value of name =",my_new_dictionary2['name'])
print("value of surname =",my_new_dictionary2['surname'])
print("value of age =",my_new_dictionary2['age'])
print("detail of shipra =",my_new_dictionary2['name'][0]
                          ,my_new_dictionary2['surname'][0]
                          ,my_new_dictionary2['age'][0]
      )
