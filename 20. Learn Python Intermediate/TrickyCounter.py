## 204. Tricky Counter Exercise ##

# adds the item in our list using a for loop

my_list = [1,2,3,4,5,6,7,8,9,10]

# need something on the outside that dosen't change, if in the loop, after every run, it will reset the counter to 0 each time it runs through the list
counter = 0

for num in my_list:
    counter = counter + num

print(counter)
