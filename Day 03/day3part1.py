fileobj = open("Day 03\inputday3.txt","r")
common_item=[]
sum=0
for line in fileobj.readlines():
    line = line.strip("\n")
    comp1 = line[:(len(line)//2)]
    comp2 = line[(len(line)//2):]
    # print(len(comp1))
    for x in comp1:
        if x in comp2:
            common_item.append(x)
            break
# print(common_item)
for item in common_item:
    if ord(item) >=97:
        # print(ord(item)-96)
        sum+=(ord(item)-96)
    else:
        # print(ord(item)-38)
        sum+=(ord(item)-38)

print(sum)