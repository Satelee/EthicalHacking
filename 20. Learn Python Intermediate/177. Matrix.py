## 177. Matrix ##
# a way to describe 2D lists or multi-dimensional lists

# list inside of another list
matrix = [
    [1,5,1],
    [0,1,0],
    [1,0,1]
]

# you have the main array (outer brackets)
# and the sub-arrays (3 in this case)
# you can have multiple arrays inside other arrays

# to access a mutli-dimensional list:
print(matrix[0][1])

# here it is accessing the first item within the array (the first list of numbers) 
# then it accesses the first element of the first list contained within the array
# can keep adding [] to access more information from the array/list

######################################

## Matrix Exercise ##

# using this list: 
basket = [
    "Banana", 
    ["Apples", 
    ["Oranges"], 
    "Blueberries"]
    ];

# access "Oranges" and print it:
print(basket[1][1][0])

