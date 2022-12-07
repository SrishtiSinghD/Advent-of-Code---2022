fileobj = open("inputday4.txt","r")

lines = fileobj.readlines()

count=0

for line in lines:
    line = line.strip("\n").split(",")
 
    elf1 = [int(x) for x in line[0].split("-")]
    elf2 = [int(x) for x in line[1].split("-")]

    if ((elf1[0]<elf2[0]) and (elf1[1]<elf2[0])):
        count+=1
    elif ((elf2[0]<elf1[0]) and (elf2[1]<elf1[0])):
        count+=1

print((len(lines)-count))


