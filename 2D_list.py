### Working with 2D list ###

grades = [[10, 50, 25, 12], [245], [35, 56, 12, 32]]
# print(grades[0]) #first list in grades
# print(grades[0][1]) #second element of first list in grade

# list are dynamic
# grades.append([4]) #add and element, increseasing length
# grades.pop(1) # indexes rearranged

# grades.clear() #remove all

# iterate through 2D list
for inner_list in grades:
    for grade in inner_list:
        print(grade, end=" ")
    print()
# This will break if one elemement is not in a list

# iterate through range
for i in range(len(grades)):
    for j in range(len(grades[i])):
        print(grades[i][j], end=" ")
    print()


###Function to iterate through list ###

def print_2D(grades):
    for inner_list in grades:
        for grade in inner_list:
            print(grade, end=" ")
        print()


print_2D(grades)

# checking if list
grades = [[56, 3, 23], [45, 23, 5, 76], 87, 43, [234]]
for inner in grades:
    if isinstance(inner, list):
        for grade in inner:
            print(grade, end=" ")
        print()
    else:
        print(inner)

## FUnction to print list ###


def print2d(passed_in):
    for inner in passed_in:
        if(isinstance(inner, list)):
            for data in inner:
                print(data, end=" ")
            print()
        else:
            print(inner)


print2d(["chicken", "Mutton", [43, 12], 54, 23, "game"])

# split
data = "This is data"
print(data.split(" "))

# list comprehesion without the square bracket[] are called generator expression

###  Joins  ###

data = ['This', 'is', 'data']
print(" ".join(data))  # join only string

# join only work with strings
data = ['This', 'is', 'data', 5, 10, "okay"]
# print(" ".join(str(data))) # does not work this way
print(" ".join(str(i) for i in data))


### sorting 2D list ###
data = [[10, 2, 3], [10, 4], [4, 6000], [10]]
print(sorted(data))
# [[4, 6000], [10], [10, 2, 3], [10, 4]]
# it checks for first element in each inner list and sort accordingly
# if there is a conflict then it checks for next element and so on

# behind the scenes a comparision is done.
print([10] < [11])  # True
print([1, 10] < [1, 2])  # False

### Key fuction with list ###
data = [1, 2, 34, -5, 2, 5, -2, -5, -67, -2, 5]
print(sorted(data, key=abs))  # taking the absolute value
# [1, 2, 2, -2, -2, -5, 5, -5, 5, 34, -67]

data = [[10, 2, 3], [10, 4], [4, 5, 6], [10, 23, 12]]
print(sorted(data, key=sum))  # taking the sum of each inner list
# [[10, 4], [10, 2, 3], [4, 5, 6], [10, 23, 12]]

# Creating custom Key
data = [[10, 2, 3], [10, 4], [4, 5, 10, 10, 10, 10, 10,
                              234, 43, 6], [10, 23, 12, 43, 23, 12], [10]]


def avg(data):
    return sum(data)/len(data)


print(sorted(data, key=avg))
