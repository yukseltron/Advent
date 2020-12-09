from string import digits

f = open("input.txt", "r")
bags = {}
qualifies = {}

counter = 0
for x in f:
    x = x.replace("\n","")
    x = x.replace(" ","")
    x = x.replace(".","")
    x = x.replace("bags","")
    x = x.replace("bag","")
    result = ''.join([i for i in x if not i.isdigit()])
    string = result.split("contain")
    string[1] = string[1].split(",")
    bags[string[0]] = string[1]



def find(rule):
    for i in bags[rule]:
        if "shinygold" in i:
            return True
        elif "noother" in i:
            return False
        else:
            find(i)

for b in bags:
        if find(b) == True:
            qualifies[b] = True

print(len(qualifies))
