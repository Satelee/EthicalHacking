## 178. List Methods ##
# method is a function that is owned by something & is specific to its data type
# everything in python is an object (number, list, variable)

basket = [1,2,3,4,5]

# adding items to the end of a list
basket.append(100)
# append changes the list in place (dosen't produce a value, it just appends 100 to basket)
# once a value is appended, then you can assign it to a new list

new_list = basket
print(basket)
print(new_list)

# adding items anywhere into the list
basket2 = [1,2,3,4,5]

# adds 100 into the 4th index of the list
basket2.insert(4, 100)

# adding an item to a list does not create a copy of it, it simply modifies the current list values
print(basket2)

# extend the list to include new values at the end
basket3 = [1,2,3,4,5]

# takes in an iterable (something you can loop over) like another list
basket3.extend([100,101])
print(basket3)

# removing the last item from a list
basket.pop()
print(basket)

# removes item from specified index
basket.pop(0)
print(basket)

# pop returns a value and can work with new_lsit = basket.pop(4)
# this does not work for other methods as they do not return anything
# by hovering over each method, you can see what they return
    # 'None' means they reutrn nothing and the method won't produce anything, it only modifies the original content

# removing item based on value
basket2.remove(4)
print(basket2)

# remove everything contained within a list
basket3.clear()
print(basket3)

## 179. List Methods 2 ##
# keyword is something used in python that already has meaning

list = ['a','b','c','d','e']

# shows the index of an item
print(list.index('d'))

# can also include start and stop values so it searches for the item within those values
print(list.index('c', 0, 4))

# returns a boolean if the item is in the list or not
# this keyword can also be used to find letters in strings
    # e.g. ('i' in 'hi my name is')
print('d' in list)
print('x' in list)

list2 = ['a', 'b', 'b', 'b', 'c', 'd', 'e']

# counts how many of the chosen value is within the list
print(list2.count('b'))

## 180. List Methods 3 ##

alphabet = ['a', 'x', 'c', 'b', 'd', 'e']

# sorts the list into an order (in this case, alphabetical)
alphabet.sort()
print(alphabet)

# function that does the same thing, unlike a method though, the function creates a whole new array by copying the original and modifying it
    # instead of modifying the original one and printing it
print(sorted(alphabet))

# a method that allows us to copy a list and prints it
    # .copy()

# reverses the indexes of the list
# it won't sort it for you
alphabet2 = ['z', 'e', 'r', 'x', 'y', 'a']

alphabet2.reverse()
print(alphabet2)

# if you want the list to be sorted then displayed reverse, best thing to do is to sort the list, then reverse it.
alphabet2.sort()
alphabet2.reverse()
print(alphabet2)

# list/array methods: https://www.w3schools.com/python/python_ref_list.asp
# keywords: https://www.w3schools.com/python/python_ref_keywords.asp 

######################################

## List Methods Exercise ##

# using this list, 
exercise_basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
exercise_basket.remove("Banana")

# 2. Remove "Blueberries" from the list.
exercise_basket.remove("Blueberries")
    # could also do exercise_basket.pop()

# 3. Put "Kiwi" at the end of the list.
exercise_basket.append("Kiwi")

# 4. Add "Apples" at the beginning of the list
exercise_basket.insert(0, "Apples")

# 5. Count how many apples in the basket
exercise_basket.count("Apples")

# 6. empty the basket
exercise_basket.clear()

print(exercise_basket)
