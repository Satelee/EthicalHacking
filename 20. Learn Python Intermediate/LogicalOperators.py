## 199. Logical Operators ##
# allows us to perform logic between two things
    # 'and'
    # 'or
    # 'not'
    # >
    # <
    # == 

# greater than
print(4 > 5)  # False, it is not

# less than
print(4 < 5) # True, it is

# equals to
    # cannot use one '=' as that is what is used to assign a variable in python
print('hello'== 'hello')  # True, as they both are teh same thing

# multiple operators 
print(1 < 2 < 3 < 4)    # prints true because all are true
print(1 < 2 > 3 < 4)    # it will short circuit and prints false as there is something false halfway through the statement

# greater than or equal to
print(1 >= 0)   # asking if 1 is greater than or equal to 0

# less than or equal to
print(1 <= 0)   # prints false as 1 does not equal to or is smaller than 0
print(0 <= 0)   # prints true as 0 is equal to 0

# not equal to
print(0 != 0)   # prints false as 0 == 0
print(0 != 1)   # prints true as 1 does not equal 0

# not - key word & function (basically get the opposite)
print(not(False))   # prints true
print(not(True))    # prints false
print (not(1 == 1)) # prints false as 1 does equal to 1 but 'not' prints the opposite

######################################

## 200. Logical Operators Exercise ##

is_magician = False
is_expert = True

# 1. check if magician AND expert:
if is_magician and is_expert:
    print('you are a master magician')

# 2. check if magician but not expert:
elif is_magician and not is_expert:
    print('at least you\'re getting somehwere')

# 3. if you're not a magician:
else:
    print('you need magic powers')

# or you could write the else statement like:
# elif not is_magician:
    # print('you need magic powers')