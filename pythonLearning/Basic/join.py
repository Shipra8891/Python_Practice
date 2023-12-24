# join - this is a fucntion which is used to convert the different
# datatype  / collection / data structure
# to String
# output of join function is String

l = ["Shipra","is","good","person"]
print("original datatype or data structure",l)

print("".join(l)) # no delimiter means what is seprator between two words
print(" ".join(l)) # deimiter is space
print("-".join(l)) # delimeter is dash
print(" use of join tuple")

t = ("Shipra","is","good","person")
print("".join(t))
print(" ".join(t))
print("-".join(t))

u = ("Shipra","is","good","person")
delimiter = ','
print(delimiter.join(t))
