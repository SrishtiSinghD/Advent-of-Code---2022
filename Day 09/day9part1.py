fileobj = open("Day 09/inputday9.txt","r")

grid={0:[[0,'#']]}
head=[0,0]
tail=[0,0]

def update():
    new=[]
    new.append(tail[1])
    new.append('#')
    if tail[0] in grid.keys():
        if new not in grid[tail[0]]:
            grid[tail[0]].append(new)
    else:
        grid[tail[0]]=[]
        grid[tail[0]].append(new)

def check ():
    if head[0] == tail[0]:
        if tail[1]+2 == head[1]:
            tail[1] = tail[1]+1
            update()
            return
        if tail[1]-2 == head[1]:
            tail[1] = tail[1]-1
            update()
            return
    if head[1] == tail[1]:
        if tail[0]+2 == head[0]:
            tail[0] = tail[0]+1
            update()
            return
        if tail[0]-2 == head[0]:
            tail[0] = tail[0]-1
            update()
            return
    if abs(head[0]-tail[0])>=2 or abs(head[1]-tail[1])>=2:
        if head[1] > tail[1]:
            if head[0] > tail[0]:
                tail[0]+=1
                tail[1]+=1
                
            else:
                tail[0]-=1
                tail[1]+=1
            
        else:
            if head[0] > tail[0]:
                tail[0]+=1
                tail[1]-=1
            else:
                tail[0]-=1
                tail[1]-=1
        update()
        return
    

for line in fileobj.readlines():
    instruction = line.strip("\n").split()
    
    direction = instruction[0]
    steps = int(instruction[1])

    for step in range(steps):
        if direction == "U":
            head[1]=head[1]+1
        elif direction == "D":
            head[1] = head[1]-1
        elif direction == "L":
            head[0] = head[0]-1
        else:
            head[0] = head[0]+1
    
        check()

count=0

for key in grid.keys():
    count+=len(grid[key])

print(count)