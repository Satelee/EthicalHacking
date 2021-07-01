## 201. is vs == ##
# == checks for equality of a value
# it will convert two different values into the same value and compares them
# you should be checking two of the same types together 


# challenge - guess the output of these statements:
print(True == 1)    # true
print('' == 1)      # false
print([] == 1)      # false
print(10 == 10.0)   # true
print([] == [])     # true

# is checks if the location in memory where the value is stored is the same

print(True is True)
print('1' is 1)     # this would print false as the different data types are stored in different areas of memory
print([] is [])     # also false as when a new list is created, it is stored in different places

# numbers and strings are types in memory that are all stored in one location 
# while lists and arrays are data structures so when a new one is created, it is stored in a new location

a = [1,2,3]
b = [1,2,3]
print(a == b)   # this would print true as '==' focuses on the values itself

# is checks for the exact thing you may be looking for while '==' checks to see if the values are equal

