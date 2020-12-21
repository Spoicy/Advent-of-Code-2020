import re

f = open('advent4.txt')
lines = f.readlines()
fields = [['byr:', '^(19[2-9][0-9]|200[0-2])$'],
    ['iyr:', '^(201[0-9]|2020)$'],
    ['eyr:', '^(202[0-9]|2030)$'],
    ['hgt:', '^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$'],
    ['hcl:', '^#[0-9a-f]{6}$'],
    ['ecl:', '^(amb|blu|brn|gry|grn|hzl|oth)$'],
    ['pid:', '^[0-9]{9}$']]
i = 0
fieldCount = 0
correctPassportCount = 0

while i < len(lines):
    if lines[i].isspace():
        if fieldCount == 7:
            correctPassportCount += 1
        fieldCount = 0
    elif i == len(lines) - 1: 
        print "yoinkular"
        for field in fields:
            if field[0] in lines[i]:
                start = lines[i].find(field[0]) + 4
                end = lines[i].find(" ", start)
                if end == -1:
                    end = len(lines[i])
                verifyString = lines[i][start:end]
                if bool(re.match(field[1], verifyString)):
                    fieldCount += 1
        if fieldCount == 7:
            correctPassportCount += 1
    else:
        for field in fields:
            if field[0] in lines[i]:
                start = lines[i].find(field[0]) + 4
                end = lines[i].find(" ", start)
                if end == -1:
                    end = len(lines[i])-2
                verifyString = lines[i][start:end]
                if bool(re.match(field[1], verifyString)):
                    fieldCount += 1
    i += 1

print correctPassportCount
