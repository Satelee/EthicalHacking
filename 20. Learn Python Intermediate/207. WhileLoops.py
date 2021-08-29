## 207. While Loops ##
# while condition: 

i = 0

while i < 50:
    print(i)
    break   # keyword that ends the while loop, essentially saying to python "at this point, break out of the while loop"

# it will constantly loop as 0 is always going to be less than 50
# inifite loop - program doesn't know when to stop
    # can be very dangerous so be careful

# ensure loop ends at 50

e = 0
while e < 50:
    print(e)
    e += 1   # stops at 50 as you incrimeted 'e' by 1 each time it went through the while loop

# can break out of a while loop as long as you can change the condition to false or use break

# can have else blocks in while loops
t = 0
while t < 50:
    print(t)
    t += 1
else:
    print('done with all the numbers')

# while t < 50, keep looping through the while loop, but once it's done, print the statement in 'else'
# else statement will only execute if there isn't a break statement
     # if while condition turns to false, then it keeps going into the else statement
     # if there is a break, it will break out of the entire loop

## 208. While Loops 2 ##
my_list = [1,2,3]

for item in my_list: 
    print(item)

c = 0
while c < len(my_list):
    print(my_list[c])
    c += 1

# while loops are very flexible, can loop more than 3 times if wanted to making them more powerful
    # with while loop, you have to create variable and increment it to avoid infinite loop
# for loops are simpler 

# for simple loops or iterating over iterable objects, use for loops
# if your unsure how many times you need to loop over something/unsure how long it will take, use a while loop
    # useful for tasks where looping can happen for a long time

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break