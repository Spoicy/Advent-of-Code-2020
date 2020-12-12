f = open('advent1.txt')
expenses = f.readlines()
i = 0
j = 0
l = 0

while i < len(expenses):
    while j < len(expenses):
        while l < len(expenses):
            sum = int(expenses[i]) + int(expenses[j]) + int(expenses[l])
            if sum == 2020:
                multiply = int(expenses[i]) * int(expenses[j]) * int(expenses[l])
                print multiply
                exit()
            l += 1
        j += 1
        l = 0
    i += 1
    j = 0
