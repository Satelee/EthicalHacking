## 197. Ternary Operator ##
# can also be called 'conditional expressions'
# is an operation that evaluates to something based on the condition being true or not
# same as an if-else statement, but it is a shortcut

# condition_if_true if condition else condition_if_false
    # if checks condition, if it is true it will do 'condition_if_true' ottherwise it will do 'condition_if_false'

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)