from collections import deque
directions={'S':[],'.':[],'|':[(1,0),(-1,0)],'-':[(0,1),(0,-1)],'L':[(-1,0),(0,1)],'J':[(-1,0),(0,-1)],'7':[(1,0),(0,-1)],'F':[(1,0),(0,1)]}
grid=[]
with open('day10.txt') as file:
    for line in file:
        grid.append(line)
q=deque()
visited=set()
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j]=='S':
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                if 0<=i+dr<len(grid) and 0<=j+dc<len(grid[i]) and (dr*-1,dc*-1) in directions[grid[i+dr][j+dc]]:
                    visited.add((i+dr,j+dc))
                    q.append((i+dr,j+dc,1))
res=0
while q:
    row,col,moves=q.popleft()
    res=max(res,moves)
    for dr,dc in directions[grid[row][col]]:
        if 0<=row+dr<len(grid) and 0<=col+dc<len(grid[row]) and (row+dr,col+dc) not in visited:
            if (dr*-1,dc*-1) in directions[grid[row+dr][col+dc]]:
                visited.add((row+dr,col+dc))
                q.append((row+dr,col+dc,moves+1))
print(res)