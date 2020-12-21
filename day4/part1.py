f = open('advent4.txt')
lines = f.readlines()
fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
i = 0
fieldCount = 0
correctPassportCount = 0

while i < len(lines):
    if lines[i].isspace():
        if fieldCount == 7:
            correctPassportCount += 1
        fieldCount = 0
    elif i == len(lines) - 1: 
        for field in fields:
            if field in lines[i]:
                fieldCount += 1
        if fieldCount == 7:
            correctPassportCount += 1
    else:
        for field in fields:
            if field in lines[i]:
                fieldCount += 1
    i += 1

print correctPassportCount
