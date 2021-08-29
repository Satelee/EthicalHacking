## 167. Formatted Strings ##

# adding 'f' to the begining of a print statement and including all variables in {}, it lets python kknow to format the string.
name = 'Jacob'
age = 26

print(f'Hi {name}! You are {age} years old.')

# another way is:
print("Hi {}! You are {} years old".format("Melanie", "37"))
# done by order, whatever variable comes first gets printed first.

# to print based on created variable, it has to be done like this:
print("Hi {}! You are {} years old".format(name, age))

# if you want to re-order variables (put name where age is and age where name is):
print("Hi {1}! You are {0} years old".format(name, age))
# this is because computers start counting from 0, and therefore 'name' is considered '0' and 'age' is considered '1'

# you can also create new variables within the formatting but need to include variable name within {}
print("Hi {name2}! You are {age2} years old".format(name2 = 'Zach', age2 = '30'))

######################################

## Formatted Strings Exercise ##

# 1. What would be the output of the below 4 print statements? 
    # Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))
    # Hello Cindy, your balance is 50.

print("Hello {0}, your balance is {1}.".format("Cindy", 50))
    # Hello Cindy, your balance is 50.

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
    # Hello Cindy, your balance is 50.

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
    # Hello Cindy, your balance is 50.

# 2. How would you write this using f-string?
name = 'Cindy'
amount = 50
print(f'Hello {name}, your balance is {amount}.')