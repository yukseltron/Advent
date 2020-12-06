f = open("input.txt", "r")
valid = []
s = ""
rmin = 0
rmax = 127
cmin = 0
cmax = 7
maxValue = 0
minValue = 99999999999
sumValue = 0

#part 1 and part 2
while 1:
    x = f.read(1)
    if not x:
        break

    if x == 'F':
        rmax = ((rmax-rmin)/2) + rmin
    elif x == "B":
        rmin = rmax - ((rmax-rmin)/2)
    elif x == "R":
        cmin = cmax - ((cmax-cmin)/2)
    elif x == "L":
        cmax = ((cmax-cmin)/2) + cmin
    else:
        sid = (rmax * 8) + cmax
        valid.append(sid)
        maxValue = max(sid, maxValue)
        minValue = min(sid, minValue)
        sumValue += sid

        rmin = 0
        rmax = 127
        cmin = 0
        cmax = 7

answer = sum(range(minValue, maxValue + 1)) - sumValue
print "p1:",max
print "p2:",answer


