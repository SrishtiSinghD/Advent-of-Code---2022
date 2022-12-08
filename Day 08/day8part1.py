fileobj = open("Day 08\inputday8.txt","r")

forest_grid = []

for line in fileobj.readlines():
    line = line.strip("\n")
    line = [int(x) for x in line]
    forest_grid.append(line)

best_scenic_score = 0

for i in range(1,len(forest_grid)-1):
    for j in range(1,len(forest_grid)-1):
        tree = forest_grid[i][j]
        scenic_score = 1

        up=i-1
        down=i+1
        right=j+1
        left=j-1

        count=0
        while(up>=0):
            count+=1
            if forest_grid[up][j] >= tree:
                break
            up-=1
        scenic_score*=count
        count=0
        while(down<len(forest_grid)):
            count+=1
            if forest_grid[down][j] >= tree:
                break
            down+=1
        scenic_score*=count
        count=0
        while(left>=0):
            count+=1
            if forest_grid[i][left] >= tree:
                break
            left-=1
        scenic_score*=count
        count=0
        while(right<len(forest_grid)):
            count+=1
            if forest_grid[i][right] >= tree:
                break
            right+=1
        scenic_score*=count
        count=0

        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

print(best_scenic_score)
