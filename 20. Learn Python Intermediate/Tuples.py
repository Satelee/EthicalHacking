## 189. Tuples ##
# immutable lists 
# makes thing easier & efficient - tells other programers the information contained in a tuple should not be changed
# less flexible but more performant (faster)
     
my_tuple = (1,2,3,4,5)

# can access the index
print(my_tuple[3])

# can check to see if values exist
print(2 in my_tuple)

# when using .items() to print dictionary items, it pust the keys and values into a tuple
    # tuples are valid keys in python as they are immutable 

phone = {
    (1,2): 'contacts',
    (3,4): 'apps',
    (5,6): 'photos'
}
print(phone[(3,4)])
 
## 190. Tuples 2 ##

# tuple slicing
new_tuple = my_tuple[1:4]

print(new_tuple)

# assigning different values to different varaibles in a tuple
x,y,z, *other = (6,7,8,9,10)

print(y)
print(other)

# counts how many chosen values are in the tuple
count_tuple = (5,5,5,7,8,9)
print(count_tuple.count(5))

# index of chosen value in tuple
index_tuple = (1,2,5,6,8,9)
print(index_tuple.index(2))

# prints length of tuple
len_tuple = (1,3,5,2,4,6,10)
print(len(len_tuple))

# tuple methods: https://www.w3schools.com/python/python_ref_tuple.asp 