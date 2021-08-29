## 203. Iterables ##
# an object/collection that can be iterated over
# it can be a:
    # list
    # dictionary
    # tuple
    # set
    # string
# a collection of items

# iterate - can go one by one to check each item in the collection

user = { 
    'name': 'Golem',
    'age': 500,
    'can_swim': False
}

# prints the key by default
for key in user:
    print(key)

# to specify printing the keys
for key in user.keys():
    print(key)

# prints the key value pair in a tuple
for pair in user.items():
    print(pair)

# prints the values
for value in user.values():
    print(value)

# these allow us to iterate over dictionaries

# can use tuple unpacking to print key and values:
    # for pair in user.items():
        # key, value = pair;
        # print(key, value)

# there is a shorter way of doing this:
for key, value in user.items():
    print(key, value)
# can also use k, v (key, value) - can rename to whatever you want, whatever makes the code more readable