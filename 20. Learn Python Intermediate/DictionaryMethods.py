## 187. Dictionary Methods ##

user = {
    'number': 23,
    'welcome': 'Mel'
}

# a way to access a key/see if it exists is to use the method .get
    # will print 'None' if it doesn't exist 
print(user.get('age'))

# can also set the default value for a key
print(user.get('age', 25))

# this is saying, get 'age' from the user dictionary
    # but if age dosen't exist, set it to 25

# but if the user has age, it will apply whatever the value in the dictionary is

# another way to create dictonaries
# dictionary = dict(key=value)
user2 = dict(name='John')
print(user2)

# dictionary methods: https://www.w3schools.com/python/python_ref_dictionary.asp