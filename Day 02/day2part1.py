dict1 ={'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}

fileobj = open("inputday2.txt","r")
score = 0

for line in fileobj.readlines():
    line = line.strip("\n")
    score += dict1[line]

print(score)