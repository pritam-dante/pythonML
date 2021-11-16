#### intro to sets ####

# don't care about order
# just need to know yes or no?

backpack2 = {"sword", "apple", "banana", "pizza", "sword"}
print("sword" in backpack2)

###### counting with list comprehension #####
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips", "pizza", "frozen custard", "apple crisp", "kale chips",
            "pizza", "frozen custard", "apple crisp", "kale chips", "pizza", "frozen custard", "apple crisp", "kale chips", "banana", "apple"]

counts = [[backpack.count(item),item] for item in backpack]

print(counts)
count_unique = [[backpack.count(item),item] for item in set(backpack)]
print(count_unique)


#### counting elements with counter

from collections import Counter
print(Counter(backpack))