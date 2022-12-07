import fileinput

sum=0
top_three_sum=[0,0,0]
i=1
fileobj = open("inputday1.txt","r")


# Using fileinput.input() method
for liner in fileobj.readlines():
    line = liner.strip()
    print(i,"-->",line, (line!=""))
    i+=1
    if line != "":
        sum+=int(line)
    else:
        print("sum = ",sum)
        if sum > top_three_sum[2]:
            top_three_sum[0] = top_three_sum[1]
            top_three_sum[1] = top_three_sum[2]
            top_three_sum[2] = sum 
        elif sum > top_three_sum[1]:
            top_three_sum[0] = top_three_sum[1]
            top_three_sum[1] = sum
        elif sum > top_three_sum[0]:
            top_three_sum[0] = sum
        sum=0
fileobj.close()
n=0
for x in top_three_sum:
    n+=x
print(n)