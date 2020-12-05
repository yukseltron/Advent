f = open("input.txt", "r")
list = []
valid = {}
counter = 1
string = ""

for x in f:
    if (x != "\n"):
        string += x
    else:
        a = string.split('\n')
        b = ' '.join(map(str, a))
        c = b.split(' ')
        list.append(c)
        string = ""


#part 1
for i in list:
    i.pop()
    if len(i) == 8:
        counter += 1
        valid.append(i)
    elif (len(i) == 7):
        d = ' '.join(i)
        if "cid:" not in d:
            counter += 1
            valid.append(i

#part 2
for i in valid:
    for j in i:



print(counter)
