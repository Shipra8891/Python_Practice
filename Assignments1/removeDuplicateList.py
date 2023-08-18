# 1st approach of removing duplicate element from list ---- using  set
list_dup = [4,1,2,3,5,1,2,3,4]

print("Original list is ",list_dup)
print("Result after removing duplicates",set(list_dup))

# 2nd approach using for loop

res = []
for i in list_dup:
    if i not in res:
        res.append(i)
print("-----------------------------------------------")
print("Original list is ", list_dup)
print("Result after removing duplicates", res)




