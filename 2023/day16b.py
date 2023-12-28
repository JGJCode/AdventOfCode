import sys
sys.setrecursionlimit(1000000)
grid=[]
with open('day16.txt') as file:
    for line in file:
        grid.append(line.rstrip())
def dfs(row,col,dx,dy,visited,cache):
    if not (0<=row<len(grid)) or not (0<=col<len(grid[0])):
        return
    if (row,col,dx,dy) in cache:
        return
    visited.add((row,col))
    cache.add((row,col,dx,dy))
    if grid[row][col]=='.':
        dfs(row+dx,col+dy,dx,dy,visited,cache)
    elif grid[row][col]=='/':
        dfs(row+dy*-1,col+dx*-1,dy*-1,dx*-1,visited,cache)
    elif grid[row][col]=='\\':
        dfs(row+dy,col+dx,dy,dx,visited,cache)
    elif grid[row][col]=='-':
        if dy:
            dfs(row+dx,col+dy,dx,dy,visited,cache)
        else:
            dfs(row,col+1,0,1,visited,cache)
            dfs(row,col-1,0,-1,visited,cache)
    elif grid[row][col]=='|':
        if dx:
            dfs(row+dx,col+dy,dx,dy,visited,cache)
        else:
            dfs(row+1,col,1,0,visited,cache)
            dfs(row-1,col,-1,0,visited,cache)
res=0
for i in range(len(grid)):
    visited=set()
    dfs(i,0,0,1,visited,set())
    res=max(res,len(visited))
    visited=set()
    dfs(i,len(grid[0])-1,0,-1,visited,set())
    res=max(res,len(visited))
for i in range(len(grid[0])):
    visited=set()
    dfs(0,i,1,0,visited,set())
    res=max(res,len(visited))
    visited=set()
    dfs(len(grid)-1,i,-1,0,visited,set())
    res=max(res,len(visited))
print(res)
