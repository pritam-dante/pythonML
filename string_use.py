
#### FIll list from user Input ####
print('Sup nerd tell me your favourite veggies')
print("Hit enter after each food. r to remove and q to quit")

favs = []

while True:
    data = input()
    if str.lower(data) == "q":
        break
    elif str.lower(data) == "r":
        # print("Removing:", favs.pop()) #stack
        print("Removing:", favs.pop(0)) #queue
    else:
        favs.append(data)
    print(favs)

for food in favs:
    print("You said", food)

#stack --> first in last out or last in fast out
#queue --> first in fast out or last in last out