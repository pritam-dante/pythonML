### Intro to Dictionaries ###

# dict stores key-value pairs

emails = {
    "pritam": "pritam@gmail.com",
    "das": "das@gmail.com"
}

print(emails)
# in this case, the key is the name, email is the value.
# Data type doesn't matter at all for the value.
# Key must be a hashable --> What does this mean?
# Classes have a function __hash__ invoked when used as the key

print(hash("hello"))
# I'm not sure of exact internals on how the hash is used, but imagine it like so:
# You have an area of memory with 8 spots, and you need to store the value at some spot...
print(hash("hello") % 8)

# Almost always immutable type (should be, anyway)
# a tuple will work, list will not. a number will work

# Why use a hashtable? Extremely fast to add or look up data
# O(1) --> constant time. More elements does not mean slower unlike a sort or something


### Retrieve data from dictionary ###
print(list(emails))
print(sorted(emails))

# Since data is not nicely sequenced
# we may want to check before we try grabbing stuff

if("Pritam" in emails):
    print("emailing", emails["Pritam"])

# This may seem bad because we first check to see if its in
# Then we do another line to get the value
# but this is different than a list where we iterate to find the element
# The key is goes through hash to calculate index. Either there or not
#This is O(1)

# You may still not like the casing and in that situation there is a method


print(emails.get("Pritam"))  # returns none if not found
# optional return arg if not found
print(emails.get("PRitam", "Nai pua kelas`"))


### ADD data to DICTIONARY ###

# how to add data (3 ways here)
# indexing
emails['suman'] = "suman@gmail.com"


# update function
# best way..can add multiple dict together
emails.update({"suna": "suna@gmail.com", "blsh": 'dcjs'})


# weird variation
emails.update(kalu="kalu@gmial.com")
print(emails)

# Key must be hashable
emails[5] = "test"
emails[(1, 2)] = "yep"
# emails[[5, 3]] = "nope" #list is not hashable (mainly cuz mutable)
print(emails)


### LOOPING through KEYS ####


# dictionary is an iterable

emails = {
    "pritam": "pritam@gmail.com",
    "suna": "suna@gmail.com",
    "das": "das@gmail.com"
}


# k is a variable but k by convention for key
for k in emails:
    print(k)

# You can use the key to get the element
# Not ideal.
# One reason being the key has to be hashed to get the value associated with it.

for k in emails:
    print("index", k, "is", emails[k])


### LOOPING THROUGH KEY_VALUE PAIRS ####

for k, elem in emails.items():
    print(k, elem)

# Each iteration k will be the key and elem will be the item found at this key.


# As an example of what a hashtable can be used for, you can keep track of occurances:

conjunctions = {"but": 0, "or": 0, "so": 0, "and": 0,
                "yet": 0, "for": 0, "nor": 0}  # fanboys

completely_original_poem = """I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side"""

words = completely_original_poem.split()

for word in words:
    if(str.lower(word) in conjunctions):
        conjunctions[str.lower(word)] += 1
print(conjunctions)

# This could easily be wrapped in a function to take a msg and words to look for, returning a dict
# concept can be used to analyze documents to quantify how vulgar they are, search for phrases, etc
# dictionaries can be used to keep track of values that are hard to cal


##### SETS Explained ####


# Sets are similar to dictionaries in that the data is hashed and it is unordered.
# Sets are similar to lists in that they just contain the data and not a key-value pair
# Sets are different than lists in that you cannot have duplicates

stuff = {"sword", "rubber duck", "pizza"}
print("sword" in stuff)
print(stuff)
stuff.add("sword")
print(stuff)
# Notice only one occurance of sword even though already added


# How is a set different than a dictionary?
# For a set, each element is only one piece of data
# for a dictionary, it is a key-value pair.


# Behind the scenes, they both use hashing. The hashing is used to determine where to store the data.
# For dictionaries, the KEY is hashed
# for sets, we do not have a key, so the data itself is hashed.
# This means we cannot store something in sets that is not hashable.
# stuff.add(["blah"]) // list is not hashable

# It's important to understand the purpose of a set...
# Easily check if element in set
# such as to easily check to see if something has been tagged


# An example would be to see if a word is ever used in a phrase. Not counted (that wold be a dictionary)

conjunctions = {"but", "or", "so", "and", "yet", "for", "nor"}  # fanboys
seen = set()  # THERE'S NOT AN EMPTY SET LITERAL!! #learn something new every day
completely_original_poem = """I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side or and yet"""

words = completely_original_poem.split()

for word in words:
    if str.lower(word) in conjunctions:
        seen.add(str.lower(word))

print(seen)


######### REMOVE DUPLICATES FROM LIST / CREATE SET FROM LIST ##########


# You can remove duplicate elements from a list by converting it to a set and back.

colors = ["red", "red", "green", "green", "blue", "green", "blue", "green"]

colors[:] = list(set(colors))

# Earlier on in our life I showed some code to count each type of element in a list.

colors = ["red", "red", "green", "green", "blue", "green", "blue", "green"]
counts = [[colors.count(item), item] for item in set(colors)]

print(counts)
# This works because is iterates through the set {"red", "green", "blue"} counting each in colors


######### UNION AND INTERSECTION #########


my_fav = {"red", "green", "black", "blue", "purple"}
her_fav = {"blue", "orange", "purple", "green"}

# union

all_favs = my_fav | her_fav
print(all_favs)
# You may see + to combine lists, in which there are repeats.
# But we are not working with lists...so i'll try to focus here.


# intersection (elements shared between both)
weeding_color = my_fav & her_fav
print(weeding_color)

# There are also method versions:
all_favs = my_fav.union(her_fav)
print(all_favs)

wedding_colors = my_fav.intersection(her_fav)
print(wedding_colors)


######### DIFFERENCE AND SYMMETRIC DIFFERENCE #########


my_fav = {"red", "green", "black", "blue", "purple"}
her_fav = {"blue", "orange", "purple", "green"}

# Difference
only_my_colors = my_fav - her_fav
print(only_my_colors)  # elements in left getting rid of all in right.
# Could go other way too:
only_her_colors = her_fav - my_fav
print(only_her_colors)

# symmetric difference is like if you took colors only I liked union with colors only she liked and put em together:

symmetric = my_fav ^ her_fav
print(symmetric)

# This is like:
symmetric = only_my_colors | only_her_colors
print(symmetric)

# like union and intersection, there are method versions that return. --> .difference and .symmetric_difference
