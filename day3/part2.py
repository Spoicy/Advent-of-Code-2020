f = open('advent3.txt')
trees = f.readlines()
treeCount = 0
treeCountTotals = []
treeMultiply = 0
x = 0
y = 0
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for i in range(len(slopes)):
    while y < len(trees):
        if x >= len(trees[y])-2:
            x -= len(trees[y])-2
        treeCheck = trees[y][x]
        if treeCheck == "#":
            treeCount += 1
        x += slopes[i][0]
        y += slopes[i][1]

    treeCountTotals += [treeCount]
    treeCount = 0
    x = 0
    y = 0

print treeCountTotals
for num in range(len(treeCountTotals)):
    if num == 0:
        treeMultiply += treeCountTotals[num]
    else:
        treeMultiply *= treeCountTotals[num]

print treeMultiply