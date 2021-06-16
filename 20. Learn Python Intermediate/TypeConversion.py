## Type Convresion ##
# converting the type of our data types

print(type(str(100)))
# if we run str function on an int, it converts the int to a string

print(type(int(str(100))))
# this will take 100, convert it into a str, then convert it into a int then take the type (which is now int) and print it

a = str(100)
b = int(a)
c = type(b)
print(c)

# this converts '100' into a 'str' and stores it in 'a'
# then it a is converted into an 'int' and stored in 'b'
# then 'c' will print the data type 'b' is.
    # if you print 'b' type will be 'int'
    # if you print 'a' type will be 'str'