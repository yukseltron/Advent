import re

f = open("input.txt", "r")
valid = []
valid2 = []
s = ""

#part1
for x in f:
    if (x != "\n"):
        x = x.rstrip("\n")
        s += x + " "
    else:
        fields = s.split(" ")
        fields.pop()
        passport = {}
        for field in fields:
            data = field.split(":")
            passport[data[0]] = data[1]
        if (len(passport) == 8):
            valid.append(passport)
        elif (len(fields) == 7):
            if 'cid' not in passport.keys():
                valid.append(passport)

        s = ""

print(len(valid)+1)


#part2 working off of part 1

for v in valid:
    byr = v["byr"]
    iyr = v["iyr"]
    eyr = v["eyr"]
    hgt = v["hgt"]
    hcl = v["hcl"]
    ecl = v["ecl"]
    pid = v["pid"]

    if len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002:
        if len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020:
            if len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
                height = False
                if ("cm" in hgt):
                    hgt = hgt.split("cm")
                    if int(hgt[0]) >= 150 and int(hgt[0]) <= 193:
                        height = True
                elif ("in" in hgt):
                    hgt = hgt.split("in")
                    if int(hgt[0]) >= 59 and int(hgt[0]) <= 76:
                     height = True

                if height == True:
                    if hcl[0] == "#":
                        hcl = hcl.split("#")
                        if len(hcl[1]) == 6:
                            if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                if re.match(r"([0-9]+)", pid, re.I) and len(pid) == 9:
                                    valid2.append(v)


print(len(valid2))


