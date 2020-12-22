f = open('advent6.txt')
people = f.readlines()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i = 0
questionsSum = 0

while i < len(people):
    j = 0
    if people[i].isspace():
        questions = 26 - len(alphabet)
        questionsSum += questions
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    elif i == len(people) - 1:
        while j < len(alphabet):
            if people[i].find(alphabet[j]) != -1:
                alphabet.remove(alphabet[j])
            else:
                j += 1
        questions = 26 - len(alphabet)
        questionsSum += questions
    else:
        while j < len(alphabet):
            if people[i].find(alphabet[j]) != -1:
                alphabet.remove(alphabet[j])
            else:
                j += 1
    i += 1

print questionsSum