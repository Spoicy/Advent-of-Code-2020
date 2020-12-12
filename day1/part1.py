f = open('advent1.txt')
expenses = f.readlines()
i = 0
j = 0

while 1 == 1:
    if i < len(expenses):
        while j < len(expenses):
            sum = int(expenses[i]) + int(expenses[j])
            if sum == 2020:
                multiply = int(expenses[i]) * int(expenses[j])
                print multiply
                exit()
            j += 1
        i += 1
        j = 0
