f = open("input.txt", "r")
list = []

for x in f:
    list.append(int(x))

list.sort()

left = 0
right = 0
middle = 0

for i in list:
    for j in list:
        for k in list:
            if (i + j + k == 2020):
                left = i
                right = j
                middle = k
                break;
print( left, right, middle)

