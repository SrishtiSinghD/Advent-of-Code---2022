fileobj = open("inputday3.txt","r")

rucksacks=fileobj.readlines();
x=0
common_item=[]
sum=0

for x in range(0,len(rucksacks),3):
    elf1 = rucksacks[x].strip("\n")
    elf2 = rucksacks[x+1].strip("\n")
    elf3 = rucksacks[x+2].strip("\n")

    for c in elf1:
        if (c in elf2 and c in elf3):
            common_item.append(c)
            break

for item in common_item:
    if ord(item) >=97:
        # print(ord(item)-96)
        sum+=(ord(item)-96)
    else:
        # print(ord(item)-38)
        sum+=(ord(item)-38)

print(sum)
