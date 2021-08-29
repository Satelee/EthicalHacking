## 194. Conditional Logic ##
# booleans are really important in conditional logic
    # use if statements to determine whether something is true or false
        # # if condition exists, then either true or false. 

# creating a program for a car that automatically detects if you are able to drive it
is_old = True
is_licenced = True 

# an if statement is a conditional operation
# an expression is something that produces a value

# if is_old :
    # print('you are old enough to drive!')

# if is_old is false, it will then check to see if_licenced is true
# elif is_licenced:
    # print('you can drive now!')

# if none of the conditions above are true, it will go into the else statement
# else: 
    # print('you are not old enough to drive!')

# the program above would be very buggy as someone who is old enough but unlicenced could drive, instead:

if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')
else:
    print('you are either not old enough or are not licenced, and therefore, cannot drive.')

# you can have one if and one else statement, but multiple elif statements
    # elif condition:
    # elif condition: