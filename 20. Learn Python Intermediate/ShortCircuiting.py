## 198. Short Circuiting ##
# interpreter ignores 

is_friend = True
is_user = True

# 'or' - if either is true, run the code
# 'and' - if both are true, run the code 

# depending on which, it gets short circited because the program knows if it needs to run it or not by the first conition

if is_friend or is_user:
    print('best friends forever')

# in this case, the program sees that is_friend is true and knows that it doesn't matter if is_user is true or false, and can skip it and just print it.

is_friend1 = False
is_user1 = True

if is_friend1 and is_user1:
    print('best friends forever')

# in this case however, program can see is_friend1 is false and knows it does not need to go any further since both need to be true to count and can skip it.