## 205. range() ##
# special type of object that returns an object that produces a sequence of integers from start to stop
# not a tuple, its a different kind of object
# special kind of object that we can use to iterate overz

# if u give it just 1 number, it gives u a range from 0 to whatever number inputted 
print(range(100))

# most useful in for loops as you can iterate over a range
for number in range(0,20):     # using this range, you can loop 20 times
    print(number)

for number in range(0,10):
    print('email sent')

# if programmer doesn't need variable, change to underscore
# it would still work, but it just indicates to others that you don't care about variable, it is just to use the range for loop
# the third number is 'step' so in this case, it would skip every second number
for _ in range(0, 10, 2):
    print(_)

# for _ in range (0, 10, -1):
    # print(_)
# this will not work

# if you do bigger number first, followed by -1, it prints the numbers in the opposite direction
for _ in range(10, 0, -1):
    print(_)

# for _ in range(10, 0):
    # print(_)
# this will not work
# if you want to do something in reverse, you have to include the -1 and ensure the bigger number is first

# stepping backwards twice
for back in range(10, 0, -2):
    print(back)

# loop through the created range (1-10) which is being converted into a list, 2 times
    # quick way to create a list that has integers
for _ in range (2):
    print(list(range(10)))