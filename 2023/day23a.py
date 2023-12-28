import sys
sys.setrecursionlimit(10000000)
slopes={'>':(0,1),'<':(0,-1),'v':(1,0),'^':(-1,0)}
grid=[]
with open('day23.txt') as file:
    for line in file:
        grid.append(line)
res=0
DIRECTIONS=[(0,1),(1,0),(-1,0),(0,-1)]
def dfs(i,j,visited):
    global res
    if i==len(grid)-1:
        res=max(res,len(visited))
        return
    visited.add((i,j))
    if grid[i][j] in slopes:
        dr,dc=slopes[grid[i][j]]
        if 0<=i+dr<len(grid) and 0<=j+dc<len(grid[0]) and grid[i+dr][j+dc]!='#' and (i+dr,j+dc) not in visited:
            dfs(i+dr,j+dc,visited)
    else:
        for dr,dc in DIRECTIONS:
            if 0<=i+dr<len(grid) and 0<=j+dc<len(grid[0]) and grid[i+dr][j+dc]!='#' and (i+dr,j+dc) not in visited:
                dfs(i+dr,j+dc,visited)
    visited.remove((i,j))
dfs(0,grid[0].index('.'),set())
print(res)