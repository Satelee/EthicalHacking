## 182. List Unpacking ##
# helps you unpack a list and assign different variables for the different items within the list.
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

# the *other assigns the "other" variable to any items in a list that have not been assigned a varaible

print(a)
print(b)
print(c)
print(other)
print(d)