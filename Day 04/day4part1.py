fileobj = open("inputday4.txt","r")
count = 0

for line in fileobj.readlines():
    line = line.strip("\n").split(",")
 
    elf1 = [int(x) for x in line[0].split("-")]
    elf2 = [int(x) for x in line[1].split("-")]

    if ((elf1[0] in range(elf2[0],elf2[1]+1)) and (elf1[1] in range(elf2[0],elf2[1]+1))):
        count+=1
    elif ((elf2[0] in range(elf1[0],elf1[1]+1)) and (elf2[1] in range(elf1[0],elf1[1]+1))):
        count+=1

print(count)