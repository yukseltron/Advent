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
    print(ranges[l],letters[l], a, lists[l], a >= int(ranges[l][0]) and a <= int(ranges[l][1]))
    if (a >= int(ranges[l][0]) and a <= int(ranges[l][1])):
        counter += 1

print(counter)
