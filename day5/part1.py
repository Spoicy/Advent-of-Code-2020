f = open('advent5.txt')
seats = f.readlines()
rowMin = 0
rowMax = 127
colMin = 0
colMax = 7
i = 0
seatId = 0

for seat in seats:
    while rowMax != rowMin:
        middle = abs((rowMax - rowMin) / 2) + rowMin
        if seat[i] == "F":
            rowMax = middle
        elif seat[i] == "B":
            rowMin = middle + 1
        i += 1
    while colMax != colMin:
        middle = abs((colMax - colMin) / 2) + colMin
        if seat[i] == "L":
            colMax = middle
        elif seat[i] == "R":
            colMin = middle + 1
        i += 1
    currSeatId = rowMax * 8 + colMax
    if currSeatId > seatId:
        seatId = currSeatId
    i = 0
    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax = 7

print seatId