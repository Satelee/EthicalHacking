## 184. Dictionary ##
# its a data type and data strcture
# a way for us to organize our data just like lists
# unordered key value pair
    # unordered - not right next to each other in memory

# has a key and a value (key value pair)
# key is a string that allows us to access values
# the value can be anything we want it to be:
dictionary = {
    'a': [1,2,3],   # like a list
    'b': 'hello',   # or a string
    'x': True       # or a boolean value
}

# grabs the value of the key
print(dictionary['a'][1])
print(dictionary['b'])

# dictionaries can be put into arrays 
my_list = [
    {
        'a': [1,2,3],
        'b': 'hello',   
        'x': True       
    },
    {
        'a': [4,5,6],   
        'b': 'goodbye',   
        'x': False       
    }
]

# enters the first array, grabs the first key and displays the 3rd number
print(my_list[0]['a'][2])