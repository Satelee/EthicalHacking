## 202. For Loops ##
# allows us to run lines of code over and over again

# 'item' is a variable, and it can be anything you want it to be
    # in this case it is saying, for every item in zero to mastery, do something
    # 'zero to mastery' is known as an iterable 
        # iterable is something that is able to get looped over

for learning in 'Zero to Mastery':
    print(learning)

# this prints every item in the iterable

for numbers in [1,2,3,4]:
    print(numbers)

# the list is an iterable and we're able to loop through the list
    # this also works the same for sets and tuples

# for loops allow us to iterate over anything that has a collection of items

# nested loops
    # you can also nest conditional statements

for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)
# goes to first value of 'item', then goes to the values in 'x' and prints them with the first item in line one until 'a,b,c' are printed with '1'
# this will continue until all the letters in 'x' are printed with each number in 'item'
