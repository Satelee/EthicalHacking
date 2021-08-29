## 206. enumerate() ##
# returns an enumerate object, iterable must be another object that supports iteration
# takes an iterable object and gives you an index counter and the item of that index

# i,char = unpacking it
# i = index
    # by using i you get the index of each item in the string
for i,char in enumerate('Hello'):
    print(i, char)

# enumerate a list
for i,lis in enumerate([1,2,3]):
    print(i, lis)

# enumerate a tuple
for i,tup in enumerate((1,2,3)):
    print(i, tup)

# useful if you need the index counter for the item you are looping through

# create a script that enumerates a list of numbers from 1-10
for i,num in enumerate(list(range(100))):
    if num == 50:
        print(f'index of 50 is: {i}')
