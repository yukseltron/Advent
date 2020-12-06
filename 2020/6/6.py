f = open("input.txt", "r")


#part 1
def part1():
    sums = 0
    valid = {}
    while 1:
        x = f.read(1)
        if not x:
            break

        if x != '\n':
            valid[x] = ':D'
        else:
            y = f.read(1)
            if not y:
                sums += len(valid)

            if y != '\n':
                valid[y] = ':D'
            else:
                sums += len(valid)
                valid = {}

    return sums
#print(sums)

def part2():
    f = open("input.txt", "r")

    sums = 0
    matches = {}
    counter = 0

    for x in f:
        if x != '\n':
            if counter == 0:
                for i in x:
                    if i != '\n':
                        matches[i] = ":D"
            else:
                for i in matches.keys():
                    if i not in x:
                        del matches[i]

            counter += 1
        else:
            sums += len(matches)
            matches = {}
            counter = 0

    return sums


print(part1())
print(part2())
