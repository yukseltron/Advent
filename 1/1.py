f = open("input.txt", "r")
list = {}
count = 0

for x in f:
    list[int(x)] = count
    count += 1

def part1(max):
    for i in list:
        diff = max - i

        if diff in list:
            return (i * diff)

#print(part1(2020))

def part2(max):
    for i in list:
        diff1 = max - i
        for j in list:
            diff2 = diff1 - j

            if diff2 in list:
                return (i*j*diff2)

print(part2(2020))

