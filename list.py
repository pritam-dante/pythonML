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

backpack = ["pizza","pizza","pizza","pizza","pizza"]
print(backpack.count('pizza'))

# this can be used to prevent too many items
if(backpack.count("pizza") <5):
    backpack.append("pizza")
    print("You put a piece of pizza in your backpack")
else:
    print("You're already full")