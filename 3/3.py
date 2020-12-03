f = open("input.txt", "r")
list = []
#r = 0
counter = 0

for x in f:
    list.append(x)

#part 1
'''
for l in range(1,len(list)):
    r += 3

    if (r >= len(list[l])-1):
        r = r - (len(list[l])-1)

    if list[l][r] == "#":
        counter += 1

print(counter)
'''

#part 2

def sloper(right, left):
    r = 0
    counter = 0

    for l in range(left,len(list),left):
        r += right

        if (r >= len(list[l])-1):
            r = r - (len(list[l])-1)

        if list[l][r] == "#":
            counter += 1

    return counter

print(sloper(1,1) * sloper(3,1) * sloper(5,1) * sloper(7,1) * (sloper(1,2)))


