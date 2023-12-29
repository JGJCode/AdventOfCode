from collections import deque
grid=[]
with open('day21.txt') as file:
    for line in file:
        grid.append(line.rstrip())
q=deque()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='S':
            q.append((i,j,0))
visited=set()
res=set()
DIRECTIONS=[(0,1),(1,0),(0,-1),(-1,0)]
while q:
    row,col,moves=q.popleft()
    if moves>64:
        break
    if moves%2==0:
        res.add((row,col))
    for dr,dc in DIRECTIONS:
        if 0<=row+dr<len(grid) and 0<=col+dc<len(grid[0]) and grid[row+dr][col+dc]!='#' and (row+dr,col+dc) not in visited:
            q.append((row+dr,col+dc,moves+1))
            visited.add((row+dr,col+dc))
print(len(res))
    
