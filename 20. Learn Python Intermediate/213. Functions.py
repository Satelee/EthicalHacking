## 213. Functions ##
# def = 'define' --> used for defining functions
# make sure to call function AFTER it is defined, otherwise python will say that the function doesn't exist as it goes line by line

def say_hello():
    print("hello")

say_hello()

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
    for row in picture:
        for pixel in row:
            if (pixel == 1):
                print('*', end="")
            else:
                print(' ', end="")
        print('')

show_tree()
show_tree()
show_tree()

# memory location of where the function is stored
print(show_tree)