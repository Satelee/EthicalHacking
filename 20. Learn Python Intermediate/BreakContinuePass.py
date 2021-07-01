## 209. break, continue, pass ##

# break - breaks out of the current & closing loop
list1 = [1,2,3]

# for loop
for num in list1:
    print(num)
    break
# while loop
m = 0
while m < len(list1):
    print(list1[m])
    m += 1
    break

# continue - continue onto the top of the enclosing loop
list2 = [4,5,6]

# for loop
for value in list2:
    print(value)
    continue

# while loop
p = 0
while p < len(list2):
    print(list2[p])
    p += 1
    continue
# will not work if continue is put above the conditions/functions as it'll continue starts the loop again from the top, meaning it will only go to the top line and nothing below it

# pass - does nothing, just passes to the next line, good way to have a placeholder while coding
list3 = [7,8,9]

# for loop
for integer in list3:
    # thinking about it
    pass

# while loop
r = 0
while r < len(list3):
    # thinking about it
    pass