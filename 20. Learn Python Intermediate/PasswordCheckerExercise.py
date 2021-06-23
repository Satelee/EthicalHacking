## 174. Password Checker Exercise ##

# checks length of password and displays it.

# inputs
username = input('Enter your username: ')
password = input('Enter your password: ')

# functions
password_length = len(password)     # calculates length of password
hidden_password = '*' * password_length     # turns password to '*' using the length

# output
print(f'Hello there {username}! Your password, {hidden_password}, is {password_length} letters long.')
