## 211. What is good code? ##

# 1. Clean #
# using spaces ot make sure code is clean
# every line is easily readable with no extra stuff

# 2. Readability #
# ensure code is easy to understand for not only you but others as well
# using variable names that make sense
# using comments to make sure everything in the code makes sense to all

# 3. Predictability #
# having predictable code that is easy to understand is important
# no point using complex libraries and functions to make yourself look smarter and over-complicate things, better to keep it simple

# 4. DRY (Don't Repeat Yourself)
# don't want to have repetitive code

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# iterate over picture:
    # if 0 -> print ' '
    # if 1 -> print *

# makes it so if you need to change either variable, it is done only in one place.
fill = "*"
empty = ' '

for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end="")
        else:
            print(empty, end="")
    print('')