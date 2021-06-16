## 164. Strings ##
# strings are just a piece of text written by placing them in single or double quotation marks
# can input numbers and special characters as well

print(type('hi, hello there'))  # prints 'str' = string

# assigning strings to varaibles 
username = 'supercoder'
password = "supersecret"

print(username)
print(password)

# three single quotes used for multi-line strings
long_string = '''
WOW
O O
---
'''
print(long_string)


## 165. String Concatination ##
# add two strings together by using '+' sign 

first_name = "Satele"
last_name = "Ephyra"
full_name = first_name + ' ' + last_name    # quotation in middle acts as a space
print(full_name)

# can also do it like this:
print('hello' + ' Satele')    # extra space before 'Satele' to include space between 'hello & 'Satele'   

# string concatination only work with strings.
    # print('Satele' + 2) will not work