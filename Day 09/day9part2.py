fileobj = open("Day 09/inputday9.txt","r")

grid={0:[[0,'#']]}
knot = {0:[0,0],1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0],6:[0,0],7:[0,0],8:[0,0],9:[0,0]}

def update():
    new=[]
    new.append(knot[9][1])
    new.append('#')
    if knot[9][0] in grid.keys():
        if new not in grid[knot[9][0]]:
            grid[knot[9][0]].append(new)
    else:
        grid[knot[9][0]]=[]
        grid[knot[9][0]].append(new)

def check(i):
    if knot[i-1][0] == knot[i][0]:
        if knot[i][1]+2 == knot[i-1][1]:
            knot[i][1] = knot[i][1]+1
            if i==9:
                update()
            return
        if knot[i][1]-2 == knot[i-1][1]:
            knot[i][1] = knot[i][1]-1
            if i==9:
                update()
            return
    if knot[i-1][1] == knot[i][1]:
        if knot[i][0]+2 == knot[i-1][0]:
            knot[i][0] = knot[i][0]+1
            if i==9:
                update()
            return
        if knot[i][0]-2 == knot[i-1][0]:
            knot[i][0] = knot[i][0]-1
            if i==9:
                update()
            return
    if abs(knot[i-1][0]-knot[i][0])>=2 or abs(knot[i-1][1]-knot[i][1])>=2:
        if knot[i-1][1] > knot[i][1]:
            if knot[i-1][0] > knot[i][0]:
                knot[i][0]+=1
                knot[i][1]+=1
                
            else:
                knot[i][0]-=1
                knot[i][1]+=1
            
        else:
            if knot[i-1][0] > knot[i][0]:
                knot[i][0]+=1
                knot[i][1]-=1
            else:
                knot[i][0]-=1
                knot[i][1]-=1
        if i==9:
            update()
        return
    

for line in fileobj.readlines():
    instruction = line.strip("\n").split()
    
    direction = instruction[0]
    steps = int(instruction[1])

    for step in range(steps):
        if direction == "U":
            knot[0][1]=knot[0][1]+1
        elif direction == "D":
            knot[0][1] = knot[0][1]-1
        elif direction == "L":
            knot[0][0] = knot[0][0]-1
        else:
            knot[0][0] = knot[0][0]+1
    
        for i in range(1,10):
            check(i)

count=0

for key in grid.keys():
    count+=len(grid[key])

print(count)