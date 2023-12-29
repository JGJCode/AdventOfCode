import sys
sys.setrecursionlimit(10000000)
grid=[]
with open('day23.txt') as file:
    for line in file:
        grid.append(line)
DIRECTIONS=[(0,1),(1,0),(-1,0),(0,-1)]
res=0
def dfs(i,j,visited):
    global res
    if i==len(grid)-1:
        res=max(res,len(visited))
        return
    visited.add((i,j))
    for dr,dc in DIRECTIONS:
        if 0<=i+dr<len(grid) and 0<=j+dc<len(grid[0]) and grid[i+dr][j+dc]!='#' and (i+dr,j+dc) not in visited:
            dfs(i+dr,j+dc,visited)
    visited.remove((i,j))
dfs(0,grid[0].index('.'),set())
print(res)