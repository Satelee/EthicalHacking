## 168. String Indexes ##
# str = stored in memeory as an ordered sequence of characters, essentially a piece of text.


# string 'me me me' has an index of 7 as there is 7 characters
selfish = 'me me me'
         # 01234567

print(selfish[0])
# prints whatever letter is in the index of 0 within selfish ('m')

print(selfish[4])
# prints whatever letter is in the index of 4 within selfish ('e')

print(selfish)
# prints the entire string

# when using [::] in python:
    # first value is start (where do you want me to look?)
    # second value is stop (where do you want me to stop the string?)
    # third value is stepover (step over a certain amount of values, default is 1 as it goes through one value at a time)

# example of using stop
numbers = '01234567'
         # 01234567
print(numbers[0:3])
# it will print the numbers between 0-3 (0,1,2)

# example of stepover
numbers = '01234567'
         # 01234567
print(numbers[0:8:2])
# it will print the numbers between 0-8 (1,2,3,4,5,6,7) but, it will skip over every second number (0,2,4,6)

# starting with no stop or step value
numbers = '01234567'
         # 01234567
print(numbers[1:])
# starts at 1 and, as there is no value in stop or stepover, it will continue as usual.

# stopping with no start or stop value
numbers = '01234567'
         # 01234567
print(numbers[:5])
# stop at 5 and, as there is no value in start or stepover, it will run as usual, just stop at 4.

# stepping with no start or stop value
numbers = '01234567'
         # 01234567
print(numbers[::3])
# steps to every 3 values and, as there is no start or stop value, it will go with defaults (start at 0, end when string ends.)


# including negatives
numbers = '01234567'
         # 01234567
print(numbers[-1])      # prints 7
# negative index in python means 'start at end of string'

numbers = '01234567'
         # 01234567
print(numbers[-3])      # prints 5

# printing a string backwards
numbers = '01234567'
         # 01234567
print(numbers[::-1])
# need to include both collons to indicate the default start and stop value and change step to -1 to print a string backwards. (7, 6, 5, 4, 3, 2, 1, 0)
# you can also do -2 for step, and it will print every second character of the string backwards (7, 5, 3, 1)

##########################################

## String Indexes Exercise ##

# Guess the output of each print statement before you click RUN!

python = 'I am PYHTON'
        # 012345678910


print(python[1:4])
    # am

print(python[1:])
    # am PYTHON

print(python[:])
    # I am PYTHON

print(python[1:100])
    # am PYTHON

print(python[-1])
    # N

print(python[-4])
    # H

print(python[:-3])
    # I am PYTH

print(python[-3:])
    # TON

print(python[::-1])
    # NOHTYP ma I