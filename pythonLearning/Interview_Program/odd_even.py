mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mylist2 = [1, 2, 3, 44, 55, 66, 7, 8, 9]


def filter_odd_even(a_list):
    even_list = []
    odd_list = []

    for l in a_list:
        if l % 2 == 0:
            even_list.append(l)
        else:
            odd_list.append(l)

    print(even_list)
    print(odd_list)
    print(f"Even list is : {even_list}")
    print(f"Odd list is : {odd_list}")


filter_odd_even(mylist1)
filter_odd_even(mylist2)
