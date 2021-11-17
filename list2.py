### Reverse a list ###
data = [0, 1, 2, 3, 4, 5, ]
# data.reverse() #we can't print it directly cz it returns none

# we can make a copy and then print that
data_copy = data[:]
data_copy.reverse()
# print(data_copy, data)

# reverse
me = "pritam"
you = "monika"

# print(me,you)
# swap
me, you = you, me

# swap with temp variable
temp = me
me = you
you = temp

# print(me , you)

data1 = ["a", "b", "c", "d", "e", 'f', "g"]
index = 1  # swapping the second nd last second
index = 0  # swapping the frst nd last element

# print(data1[index], data1[-index -1])

data1[index], data1[-index-1] = data1[-index - 1], data1[index]
# print(data1[index], data1[-index -1])

data2 = ["a", "b", "c", "d", "e", 'f', "g", "h", "i"]

for i in range(len(data2) // 2):
    data2[i], data2[-i-1] = data2[-i-1], data2[i]
# print(data2)

data3 = ["a", "b", "c", "d", "e", 'f', "g", "h", "i"]
data_reversed = [] #reversing with a new list
for item in reversed(data3):
    data_reversed.append(item)
# print(data3)
# print(data_reversed)

data4 = ["a", "b", "c", "d", "e", 'f', "g", "h", "i"]

data4[:] = data4[::-1]
print(data4)

#reverse the contents of sub list
mylist = [[1,2,3],[4,5,6,5,4],[8,9]]
reve = [item[::-1] for item in mylist]
print(reve)

## reversing the contents and order of sub lists
mylist = [[1,2,3],[4,5,6,5,4],[8,9]]
reve = [item[::-1] for item in mylist][::-1]
# print(reve)
