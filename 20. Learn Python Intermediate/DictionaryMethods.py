## 187. Dictionary Methods ##

user1 = {
    'number': 23,
    'welcome': 'Mel'
}

# a way to access a key/see if it exists is to use the method .get
    # will print 'None' if it doesn't exist 
print(user1.get('age'))

# can also set the default value for a key
print(user1.get('age', 25))

# this is saying, get 'age' from the user dictionary
    # but if age dosen't exist, set it to 25

# but if the user has age, it will apply whatever the value in the dictionary is

# another way to create dictonaries
# dictionary = dict(key=value)
user2 = dict(name='John')
print(user2)

## 188. Dictionary Methods 2 ##
# like in lists, you can use 'in' to see if a key is located within a dictionary
# if yes it will respond with True, if not it will respond in False (boolean oeprators)

search = {
    'box': 'here!',
    'bucket': 'not here',
    'shelf': 'not here either'
}

print('bucket' in search)
print('key' in search)

# checks the keys in a dictionary
print('box' in search.keys())
print('cupboard' in search.keys())

# checks the values in a dictionary
print('not here' in search.values())
print('over here' in search.values())

# item grabs entire item 
print(search.items())

# clears dictionary & prints empty dictionary
clearme = {
    123: 'please',
    456: 'clear',
    789: 'me'
}

clearme.clear()
print(clearme)

# copy a dictionary
copy1 = {
    321: 'copying',
    654: 'is',
    987: 'fun'
}

copy2 = copy1.copy()
print(copy1.clear())    # clears the first dictionary but prints the copy made
print(copy2)

# remove a key from a dictionary
removeme = {
    'books': 4,
    'apple': 5,
    'charger': 2
}

print(removeme.pop('apple'))    # it will return the removed value
print(removeme)     # now you can see apple no longer exsists 

# randomly removes a key pair as dictionaries are unordered
    # useful to destructively iterate over a dictionary
print(removeme.popitem())   # charger is removed
print(removeme)

# update a key value
updateuser = {
    'name': 'Sam',
    'age': 23,
    'country': 'America' 
}

print(updateuser.update({'country': 'Australia'}))
print(updateuser)

# can be used to add new values
print(updateuser.update({'postcode': 6074}))
print(updateuser)

# dictionary methods: https://www.w3schools.com/python/python_ref_dictionary.asp 

###################################

## Dictionary Methods Exercise ##

# 1. Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
    'age': 23,
    'username': 'IamJonah',
    'weapons': ['sword', 'shield'],
    'is_active': True,
    'clan': 'Round Table'
}

# 2. iterate and print all the keys in the above user.
print(user.keys())

# 3. Add a new weapon to your user
user['weapons'].append('great sword')
print(user)

# 4. Add a new key to include 'is_banned'. Set it to false
user.update({'is_banned': False})
print(user)

# 5. Ban the user by setting the previous key to True
user.update({'is_banned': True})
# can also be done: user['is_banned'] = True
print(user)

# 6. create a new user2 my copying the previous user and update the age value and username value. 
user2 = user.copy()

user2.update({'age': 35, 'username': 'Gaming_with_Luke'})
print(user2)