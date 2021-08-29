## 196. Truthy vs Falsey ##
# python automatically converts data into boolean opreators at an if statement

# truthy value, because if we run the bool conversion operator, it evaluates the data to be ture
print(bool('hello'))
print(bool(5))

# falsey values
print(bool(''))
print(bool(0))

password = '123'
username = 'johnny'

if password and username:
    print('you can log in.')
else:
    print('please enter a username and password to continue.')

# what truthy and falsy is:  https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false 