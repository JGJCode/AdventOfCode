import sys
import time
start=time.time()
sys.setrecursionlimit(1000000)
grid=[]
with open('day16.txt') as file:
    for line in file:
        grid.append(line.rstrip())
visited=set()

cache=set()
def dfs(row,col,dx,dy):
    if not (0<=row<len(grid)) or not (0<=col<len(grid[0])):
        return
    if (row,col,dx,dy) in cache:
        return
    visited.add((row,col))
    cache.add((row,col,dx,dy))
    if grid[row][col]=='.':
        dfs(row+dx,col+dy,dx,dy)
    elif grid[row][col]=='/':
        dfs(row+dy*-1,col+dx*-1,dy*-1,dx*-1)
    elif grid[row][col]=='\\':
        dfs(row+dy,col+dx,dy,dx)
    elif grid[row][col]=='-':
        if dy:
            dfs(row+dx,col+dy,dx,dy)
        else:
            dfs(row,col+1,0,1)
            dfs(row,col-1,0,-1)
    elif grid[row][col]=='|':
        if dx:
            dfs(row+dx,col+dy,dx,dy)
        else:
            dfs(row+1,col,1,0)
            dfs(row-1,col,-1,0)
dfs(0,0,0,1)
print(len(visited))
print(time.time()-start)