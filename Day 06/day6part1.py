fileobj = open("Day 06\inputday6.txt","r")

buffer = fileobj.readlines()[0].strip("\n")
# print(len(buffer))
marker = []

for i in range(0,len(buffer)-3):
    marker.append(buffer[i])
    for j in range(1,4):
        if buffer[i+j] in marker:
            marker.clear()
            break
        else:
            marker.append(buffer[i+j])
    if len(marker)==4:
        print(i+j+1)
        break