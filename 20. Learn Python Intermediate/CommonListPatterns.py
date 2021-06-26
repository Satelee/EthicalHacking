##  181. Common List Patterns ##

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
# you can reverse a string use string slicing:
print(basket[::-1])
# in this case, since we've already reversed it using .reverse() by using slicing, we are reversing it back into order
# string slicing creates a new version of the list rather than modifying the originalone stored in memory

# combining lists into a string
# create a list from a range of numbers
# quick way to generate a numbered list
print(list(range(101)))

# can be used to join a list and string together 
# join joins iterable items (lists) with the string infront of it
# used to join/create a string out of a list of items
sentence = '_'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'what'])
print(new_sentence)

# another way to do this is
sentence = '!'.join(['hi', 'my', 'name', 'is', 'what'])
print(sentence)

# can be used to add in a space between each word in a list
sentence2 = ' '.join(['hi', 'my', 'name', 'is', 'what'])
print(sentence2)