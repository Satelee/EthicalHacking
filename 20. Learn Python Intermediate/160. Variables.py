## 160. Variables ##
# store information that can be used in our programs.
    # such as user inputs like values.

# wanting to store IQ value from a test
iq = 190    # binding value to variable

# print the iq value for user to see - so they don't have to re-do the test
print(iq)

## Best practices for writing a variable ##
    # 1. snake_case - all lowercase, spaces replaced with underscores
    # 2. can be anything with letters, numbers or underscores
        # but they must start with a lowercase or underscore
    # 3. case sensitive
    # 4. don't overwrite keywords - words that already have meaning in python

# Rule 1
user_iq = 100
print(user_iq)

# Rule 2
user_iq1 = 200
    # _ at start siginifies a prviate variable
print(user_iq1)

# Rule 3
user_IQ = 170
print(user_IQ)

# Rule 4
# print = 140
# print(print)
    # this won't work as 'print' already has a meaning in python

# you can re-assign variables
user_age = iq/4
print(user_age)

ua = user_age
print(ua)


# constants - things that never change in our program
PI = 3.14   # defined by being all capital letters
print(PI)

# __ - dunder variables (two underscores), meant to be left alone

# rapid way to assign values to variables multiple times
a,b,c, = 1,2,3

print(a)
print(b)
print(c)

# good rule of thumb: make variables descrptive and make intention obvious.
# Python keyword list: https://www.w3schools.com/python/python_ref_keywords.asp