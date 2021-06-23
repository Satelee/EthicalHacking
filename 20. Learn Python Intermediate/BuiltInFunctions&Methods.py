## 170. Built-In Functions & Methods ##

# calculating length of string
print(len('helloooooo'))
# it counts as humans do from 1 instead of starting from 0

greet = 'hihiiiiiii' 
print(greet[0:len(greet)])
# the program outputs the length of greet through string slicing


# built-in methods usually start with a . such as '.format()'

quote = 'to be or not to be'

# upper method - turns string into capital letters
print(quote.upper())

# capitalize method - capitalizes first letter of a string
print(quote.capitalize())

# find method - finds first occurance of word/character within a string and displays its index number
print(quote.find('be'))

# replace method - replaces all occurance of first word/character with second word/character
print(quote.replace('be', 'me'))

# strings are immutable, meaning once they are created they cannot be changed. Therefore if we want to print a modified version of quote we need to replace it with a new varaible.
quote2 = quote.replace('be', 'bee')

# then we would need to print this modified version (quote2) for the changes to be displayed.
print(quote2)

# built-in functions: https://docs.python.org/3/library/functions.html
# built-in string methods: https://www.w3schools.com/python/python_ref_string.asp 
