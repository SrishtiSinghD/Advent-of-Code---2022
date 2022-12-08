fileobj = open("Day 08\inputtestday8.txt","r")

forest_grid = []

for line in fileobj.readlines():
    line = line.strip("\n").split()
    forest_grid.append(line)

print(forest_grid)