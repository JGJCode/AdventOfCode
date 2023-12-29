from collections import defaultdict
nodeMap=defaultdict(list)
with open('day8.txt') as file:
    lines=file.readlines()
    for i in range(2,len(lines)):
        sep=lines[i].split('=')
        lr=sep[1].split(',')
        nodeMap[sep[0][:len(sep[0])-1]].append(lr[0][2:])
        nodeMap[sep[0][:len(sep[0])-1]].append(lr[1][1:4])
directions='LRRLLRLLRRRLRRLRLRRRLRLLRLRRLRRRLRRRLRRLRRRLRLRRRLRLRRLRLRRRLRRLLRRLLLRRLRLRRRLRLRRRLRRLRRRLRLLRRLRRLRLRRRLRRRLRRLRRLLRLLRRRLRLRRLRRRLRRLRRRLRRRLLLLRRLRLRRRLRRRLLRRLLRRLRRRLRRRLRLRLLRRLRLRLRLRLRRLRLRLRRRLRRLRRLRRLRRRLRLRRRLRLRRLRLLLLRRRLLRRRLRLLRRRLRLLRRRLLRRLRLRLRLRLLLLRRLRRRLRLLRRLRRRLRRRLRLRRLRRLRLLRRRR'

dirindex=0
node='AAA'
moves=0
while node!='ZZZ':
    moves+=1
    if directions[dirindex%len(directions)]=='L':
        node=nodeMap[node][0]
    else:
        node=nodeMap[node][1]
    dirindex+=1
print(moves)