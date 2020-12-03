f = open("input.txt", "r")
lists = []
letters = []
ranges = []
length = 0
counter = 0


for x in f:
    a = x.split(":")
    b = a[0].split(" ")
    c = b[0].split("-")

    lists.append(a[1])
    letters.append(b[1])
    ranges.append(c)

length = len(lists)

for l in range(length):
    a = lists[l].count(letters[l])
    string = lists[l]
    p1 = ranges[l][0]
    p2 = ranges[l][1]
    print(string[int(p1)],p1,string[int(p2)], p2, letters[l],lists[l], string[int(p1)] == letters[l] or string[int(p2)] == letters[l])
    if ((string[int(p1)] == letters[l]) ^ (string[int(p2)] == letters[l])):
        counter += 1

#pt1
'''
for l in range(length):
    a = lists[l].count(letters[l])
    print(ranges[l],letters[l], a, lists[l], a >= int(ranges[l][0]) and a <= int(ranges[l][1]))
    if (a >= int(ranges[l][0]) and a <= int(ranges[l][1])):
        counter += 1
'''
print(counter)
