dict1 ={'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}

fileobj = open("inputday2.txt","r")
score = 0

for line in fileobj.readlines():
    line = line.strip("\n")
    score += dict1[line]

print(score)