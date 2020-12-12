import re

f = open('advent2.txt')
passwordList = f.readlines()
i = 0
passwordCollection = []
correctPasswordTotal = 0

while i < len(passwordList):
    split = re.split('[- :]', passwordList[i])
    item = [[split[0], split[1], split[2], split[4]]]
    passwordCollection = passwordCollection + item
    i += 1

for collection in passwordCollection:
    min = int(collection[0])-1
    max = int(collection[1])-1
    char = collection[2]
    password = collection[3]
    first = password[min] == char
    last = password[max] == char

    if first != last:
        correctPasswordTotal +=1

print correctPasswordTotal