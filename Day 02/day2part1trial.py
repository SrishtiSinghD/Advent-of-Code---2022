# file1 = open("Day 02\inputday2.txt","r")

# dictMe={}
# line_no=1
# for liner in file1.readlines()[0:3]:
#     print(liner)
#     liner = liner.strip("\n")
#     inp = liner.split(" ")
#     print(inp)
#     if inp[0] == 'A':
#         if line_no == 1:
#             dictMe[inp[1]]='B'
#         elif line_no == 2:
#             dictMe[inp[1]]='C'
#         else:
#             dictMe[inp[1]]='A'
#     elif inp[0] == 'B':
#         if line_no == 1:
#             dictMe[inp[1]]='C'
#         elif line_no == 2:
#             dictMe[inp[1]]='A'
#         else:
#             dictMe[inp[1]]='B'
#     else:
#         if line_no == 1:
#             dictMe[inp[1]]='A'
#         elif line_no == 2:
#             dictMe[inp[1]]='B'
#         else:
#             dictMe[inp[1]]='C'
#     line_no+=1
# file1.close()

dictMe={'X': 'A', 'Y': 'B', 'Z': 'C'}

fileobj = open("Day 02\inputday2.txt","r")
dictPoints = {'A':1,'B':2,'C':3}

win = 6
draw = 3
lost = 0
score = 0

for line in fileobj.readlines():
    line = line.strip("\n")
    inp = line.split(" ")

    if inp[0] == 'A':
        if dictMe[inp[1]] == 'A':
            score = score + dictPoints['A'] + draw
        elif dictMe[inp[1]] == 'B':
            score = score + dictPoints['A'] + win
        else:
            score = score + dictPoints['A'] + lost
    elif inp[0] == 'B':
        if dictMe[inp[1]] == 'B':
            score = score + dictPoints['B'] + draw
        elif dictMe[inp[1]] == 'C':
            score = score + dictPoints['B'] + win
        else:
            score = score + dictPoints['B'] + lost
    else:
        if dictMe[inp[1]] == 'C':
            score = score + dictPoints['C'] + draw
        elif dictMe[inp[1]] == 'A':
            score = score + dictPoints['C'] + win
        else:
            score = score + dictPoints['C'] + lost

print(score)
    