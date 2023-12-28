import math
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
nodes=[]
targets=[]
for node in nodeMap:
    if node[-1]=='A':
        nodes.append(node)
    elif node[-1]=='Z':
        targets.append(node)
nodeMoves=[]
for node in nodes:
    count=0
    moves=0
    dirindex=0
    curr=node
    while count==0:
        if directions[dirindex%len(directions)]=='L':
            curr=nodeMap[curr][0]
        else:
            curr=nodeMap[curr][1]
        dirindex+=1
        moves+=1
        if curr[-1]=='Z':
            nodeMoves.append(moves)
            count+=1
print(math.lcm(*nodeMoves))
