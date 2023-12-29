from collections import deque
pipeMap={'|':[(1,0),(-1,0)],
        '-':[(0,1),(0,-1)],
         'L':[(-1,0),(0,1)],
         'J':[(-1,0),(0,-1)],
         '7':[(1,0),(0,-1)],
         'F':[(1,0),(0,1)],}
grid=[]
with open('day10.txt') as file:
    for line in file:
        grid.append(line.rstrip())
startR=startC=-1
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='S':
            startR=i
            startC=j
DIRECTIONS=[(1,0),(-1,0),(0,1),(0,-1)]
xPoints=[startC]
yPoints=[startR]
visited={(startR,startC)}
q=deque()
for dr, dc in DIRECTIONS:
    if 0<=startR+dr<len(grid) and 0<=startC<len(grid[0]) and (dr*-1,dc*-1) in pipeMap[grid[startR+dr][startC+dc]]:
        q.append((startR+dr,startC+dc))
        break
while q:
    row,col=q.popleft()
    xPoints.append(col)
    yPoints.append(row)
    visited.add((row,col))
    for dr,dc in pipeMap[grid[row][col]]:
        if 0<=row+dr<len(grid) and 0<=col+dc<len(grid[0]) and (row+dr,col+dc) not in visited and (dr*-1,dc*-1) in pipeMap[grid[row+dr][col+dc]]:
            q.append((row+dr,col+dc))
            break
def shoelaceTheorem(xPoints,yPoints) -> int:
    xSum=xPoints[-1]*yPoints[0]
    ySum=yPoints[-1]*xPoints[0]
    for i in range(len(xPoints)-1):
        xSum+=xPoints[i]*yPoints[i+1]
        ySum+=yPoints[i]*xPoints[i+1]
    return int(1/2 *(abs(xSum-ySum)))
def picksTheorem(area) -> int:
    return area+1-(len(visited)//2)
area=shoelaceTheorem(xPoints,yPoints)
num_inside=picksTheorem(area)
print(num_inside)
