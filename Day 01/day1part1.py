import fileinput

sum=0
max_sum=-1

# Using fileinput.input() method
for line in fileinput.input(files =("Day 01\inputday1.txt")):
    if line != "\n":
        sum+=int(line)
    else:
        if sum > max_sum:
            max_sum = sum
        sum=0

print(max_sum)