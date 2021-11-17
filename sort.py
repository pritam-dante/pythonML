work_days = ["monday", "tuesday", "wednesday", "thrusday", "friday"]
copy = work_days[:]
copy.sort()  # sorting based on alphabet

# print(work_days)
# print(copy)

data = [1, 5, 3, -5, 3, -6, 1, 8]
print(sorted(data))

# use sorted when we need a copy else use sort method to modifying the original

data = [1, 5, 3, -5, 3, -6, 1, 8]  # print it in sorted reverse order
data.sort()
data.reverse()
# print(data)

print(sorted(data, reverse=True))  # second method

random = ["a", "A", "aa", "AAA", "HELLO", "b", "c", "C", "a"]
random.sort(key=len)  # sorting according to length
print(random)
print(sorted(random, key=str.lower)) #sorting according to lower 
