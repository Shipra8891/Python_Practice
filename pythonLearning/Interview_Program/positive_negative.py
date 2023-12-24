list_A = [1, 2, 3, 44, 55, 66, -2, -44, 44]
another_list = [22,33,-33,44,55,77,77,44,-77]
dusra_list =[2222,3333,1,33,4,55,66,55]

list_B = set(list_A)


def check_negative_occurence(abc):
    if len(abc) < 2:
        return False
    l2 = set(abc)
    for i in l2:
        if -i in l2:
            return True

    return False

print(check_negative_occurence(another_list))
print(check_negative_occurence(dusra_list))
