fileobj = open("inputday5.txt","r")

content = fileobj.readlines()
break_line=0

for line in content:
    if line.strip("\n")=="":
        break
    break_line+=1

# print(break_line)

stack_dict = {}

stacks = content[break_line-1].strip("\n").split()

for stack_no in stacks:
    stack_dict[stack_no]= []

total_crates=len(stack_dict)

# print(stack_dict,total_crates)

for i in range(break_line-2,-1,-1):
    crates = content[i].strip("\n").split()

    for ind in range(total_crates):
        crate = crates[ind]
        # print(crate)
        if crate[1] != "*":
            stack_dict[str(ind+1)].append(crate[1])

# print(stack_dict)
    
start = break_line+1

for line in content[start:]:
    line = line.strip("\n").split(" ")
    crates_to_be_moved = int(line[1])
    from_crate = line[3]
    to_crate = line[5]
    # print(line)

    temp_queue=[]

    for times in range(crates_to_be_moved):
        crate_temp = stack_dict[from_crate].pop()
        temp_queue.append(crate_temp)
    for time in range(crates_to_be_moved):
        crate_temp = temp_queue.pop()
        stack_dict[to_crate].append(crate_temp)

# print(stack_dict)

top_crates = []

for ind in range(1,total_crates+1):
    crate_name = stack_dict[str(ind)][-1]
    top_crates.append(crate_name)

print("".join(top_crates))