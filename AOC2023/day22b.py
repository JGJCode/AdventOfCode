from collections import defaultdict,deque
bricks=[]
with open('day22.txt') as file:
    for line in file:
        points=line.rstrip().split('~')
        bricks.append([list(map(int,points[0].split(','))),list(map(int,points[1].split(',')))])
bricks.sort(key=lambda x:x[0][2])
brickMap=[[-1]*10 for _ in range(10)]
supports=defaultdict(list)
supportedBy=defaultdict(list)
for i in range(len(bricks)):
    maxHeight=[]
    for x in range(bricks[i][0][0],bricks[i][1][0]+1):
        for y in range(bricks[i][0][1],bricks[i][1][1]+1):
            if brickMap[x][y]!=-1 and (not maxHeight or bricks[brickMap[x][y]][0][2]>bricks[maxHeight[0]][0][2]):
                maxHeight=[brickMap[x][y]]
            elif brickMap[x][y]!=-1 and bricks[brickMap[x][y]][0][2]==bricks[maxHeight[0]][0][2]:
                maxHeight.append(brickMap[x][y])
            brickMap[x][y]=i
    if not maxHeight:
        bricks[i][0][2]=abs(bricks[i][1][2]-bricks[i][0][2])+1
    else:
        bricks[i][0][2]=bricks[maxHeight[0]][0][2]+abs(bricks[i][1][2]-bricks[i][0][2])+1
        maxHeight=set(maxHeight)
        for b in maxHeight:
            supports[b].append(i)
            supportedBy[i].append(b)
res=0
for i in range(len(bricks)):
    fallen={i}
    q=deque([i])
    while q:
        brick=q.popleft()
        for b in supports[brick]:
            if all(x in fallen for x in supportedBy[b]):
                fallen.add(b)
                q.append(b)
    res+=len(fallen)-1
print(res)