f = open('advent3.txt')
trees = f.readlines()
treeCount = 0
x = 0
y = 0

while y < len(trees):
    if x >= len(trees[y])-2:
        x -= len(trees[y])-2
    treeCheck = trees[y][x]
    if treeCheck == "#":
        treeCount += 1
    x += 3
    y += 1

print treeCount