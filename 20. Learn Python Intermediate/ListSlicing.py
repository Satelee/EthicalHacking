## 176. List Slicing ##
amazon_cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes'
]
# first item to 3rd item
print(amazon_cart[0:2])

# skip every second item
print(amazon_cart[0::2])

# lists are mutable 
# can change any index contained within the list
# everytime you slice a list, it creates a copy of the original list

# changing from notebook to laptop
amazon_cart[0] = 'laptop'

# print(amazon_cart[0:3]) is what you could do OR create a new varaible 
    # new_cart = amazon_cart[0:3]

# this means the new cart is going to equal amazon cart
# amazon cart points somewhere in the memory in our machines that shows where amazon cart is
# not copying the list, just saying the value of new cart is whatever is in the memory of amazon cart
# when modifying new cart, we are changing the original amazon cart list
# to copy a list: new_cart = amazon_cart[:] - uses list slicing to copy amazon cart which will equal to new cart
new_cart = amazon_cart
new_cart[0] = 'gum'
print(amazon_cart)

######################################

## List Slicing Exercise ##

# What is the output of this code?
    # Before you clikc RUN, guess the output of each print statement!

new_list = ['a', 'b', 'c']
print(new_list[1])
# b

print(new_list[-2])
# b

print(new_list[1:3])
# ['b', 'c']

new_list[0] = 'z'
print(new_list)
# ['z', 'b', 'c']

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
# ['z', 2, 3]

print(bonus)
# [1, 2, 3, 5]