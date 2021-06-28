## 186. Dictionary Keys ##
# dictionary keys need to have a special property
    # a key needs to be immutable (key cannot change)
        # values, booleans, strings are all immutable and therefore can be keys

dictkey = {
    123: [3,2,7],
    True: 'hello there!',
    'Goodbye': False 
}

print(dictkey[123])
print(dictkey[True])
print(dictkey['Goodbye'])

# keys for dictionaries are usually something descriptive like a string
    # they also have to be unique, it can only exist once otherwise the original value is overrided 

copykey = {
    'test': 'test1',
    'test': 'test2'
}

print(copykey['test'])