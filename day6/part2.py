f = open('advent6.txt')
people = f.readlines()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i = 0
questionsSum = 0
groupStorage = []
tempGroupStorage = []
firstPerson = 1
storageCheck = 0

while i < len(people):
    j = 0
    if people[i].isspace():
        questions = len(groupStorage)
        questionsSum += questions
        groupStorage = []
        firstPerson = 1
    elif i == len(people) - 1:
        while j < len(alphabet):
            if people[i].find(alphabet[j]) != -1:
                if firstPerson:
                    tempGroupStorage += alphabet[j]
                else:
                    for letter in groupStorage:
                        if letter == alphabet[j]:
                            tempGroupStorage += alphabet[j]
            j += 1
        groupStorage = tempGroupStorage
        questions = len(groupStorage)
        questionsSum += questions
    else:
        while j < len(alphabet):
            if people[i].find(alphabet[j]) != -1:
                if firstPerson:
                    tempGroupStorage += alphabet[j]
                else:
                    for letter in groupStorage:
                        if letter == alphabet[j]:
                            tempGroupStorage += alphabet[j]
            j += 1
        firstPerson = 0
        groupStorage = tempGroupStorage
        tempGroupStorage = []
    i += 1

print questionsSum