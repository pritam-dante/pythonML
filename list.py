# append to list

healthy = ["pizza", "kfc", "Burger"]

healthy.append("Chicken")

print(healthy)

# checking if a element is in the list

print("Chicken" in healthy)
# this returns True/False. Can use in keywords within if

backpack = ["pizza", "chicken pot pie", "kale chips"]

if("pizza" in backpack):
    print("eating it")

# Remove from list
healthy = ["pizza", "kfc", "Burger"]
backpack = ["pizza", "chicken pot pie", "kale chips"]

if("pizza" in healthy):
    backpack.remove("pizza")
print(backpack)


########    LIST COMPREHENSION   ########

healthy = ["kale chips", "brocoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

backpack[:] = [item for item in backpack if item in healthy]
# slice --> [:] keep same object id
print(backpack)

# similar to this (except this one makes new variable)
healthy_backpack = []

for item in backpack:
    if item in healthy:
        healthy_backpack.append(item.upper())
        # we can use item.upper() in list comprehension also
        # [item.upper() for item in backpack if item in healthy]

print(healthy_backpack)

#### List comprehension essentials ####
squares = [i**2 for i in range(10) if i % 2 == 0]
print(squares)

# same using loops
square = []
for i in range(10):
    if(i % 2 == 0):
        square.append(i**2)
print(square)


### COUNTING ELEMENTS IN LIST ###

healthy = ["kale chips", "brocoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

print(len(healthy), len(backpack))

# count is used to count a particular element in a list

backpack = ["pizza", "pizza", "pizza", "pizza", "pizza"]
print(backpack.count('pizza'))

# this can be used to prevent too many items
if(backpack.count("pizza") < 5):
    backpack.append("pizza")
    print("You put a piece of pizza in your backpack")
else:
    print("You're already full")


### insert into list ###
workdays = ["Monday", "Tuesday", "Thrusday", "Friday", "Saturday"]
# print(workdays[2])
workdays.insert(2, "Wednesday")
# with insert method the index is also going to change
# print(workdays[2])

print(workdays)
workdays.remove("Saturday")  # when we remove by data
del workdays[0]  # when we remove by index
# del work with slicing too
popped = workdays.pop(2)
print("We just removed", popped)
print(workdays)

holidays = ["Fri", "Sat", "Sun", "Mon", "Tues", "Wed"]
holidays.append("Yoyoyoyoy")

del holidays[-1]  # always remove the last element
# delete all after friday to Tuesday ..Tuesday excluded
del holidays[holidays.index("Fri"): holidays.index("Tues")]

print(holidays)

### Removing all occurances from a list ###
bag = ["pizza", "apple", "tomato", "pizza", "mutton", "jalebi", "pizza"]
# bag.remove("pizza") # remove only one pizza
while bag.count("pizza") > 0:  # not suitable for large data
    bag.remove("pizza")
# print(bag)

bag = ["pizza", "apple", "tomato", "pizza", "mutton", "jalebi", "pizza"]
# slicing in the left means same object
# slicing in the right means assigning a copy
print(bag[2:5])

bag2 = bag[:]
bag[:] = [1, 2, 3]
print(bag)
print(bag2)

num = ["one", "two", "one", "three", "four", "five", "one", "six", "one"]

# for item in num:
#     print(item)
#     if item == "one":
#         num.remove("one")
# print(num)
#not the right way to remove item from list
#either make a copy or assign it to a new list

for item in num[:]:
    print(item)
    if item == "one":
        num.remove("one")
print(num)

# assign it to a new list
num1 = ["one", "two", "one", "three", "four", "five", "one", "six", "one"]
new_num1 = []

for item in num1:
    if item != "one":
        new_num1.append(item)
num1 = new_num1 #reasign again
print(num1)

bag2 = ["pizza", "apple", "tomato", "pizza", "mutton", "jalebi", "pizza"]
#list comprehension
print(id(bag2))
bag2[:]=[item for item in bag2 if item != "pizza"]
print(id(bag2))
print(bag2)