from collections import deque
grid=[]
with open('day21.txt') as file:
    for line in file:
        grid.append(line.rstrip())
def enlargeGrid(grid):
    for i in range(len(grid)):
        grid[i]=grid[i]*3
    grid=grid*3
    return grid
grid=enlargeGrid(enlargeGrid(grid))
DIRECTIONS=[(0,1),(1,0),(0,-1),(-1,0)]
q=deque([(len(grid)//2,len(grid[0])//2,0)])
distances={(len(grid)//2,len(grid[0])//2):0}
while q:
    row,col,moves=q.popleft()
    for dr,dc in DIRECTIONS:
        if 0<=row+dr<len(grid) and 0<=col+dc<len(grid[0]) and grid[row+dr][col+dc]!='#' and (row+dr,col+dc) not in distances:
            q.append((row+dr,col+dc,moves+1))
            distances[(row+dr,col+dc)]=moves+1
l1=l2=l3=0
for i,j in distances:
    if distances[(i,j)]<=65 and distances[(i,j)]%2==1:
        l1+=1
    if distances[(i,j)]<=65+131 and distances[(i,j)]%2==0:
        l2+=1
    if distances[(i,j)]<=65+2*131 and distances[(i,j)]%2==1:
        l3+=1
CONSTANT=(26501365-65)//131
c=l1
b=(4*l2-3*l1-l3)//2
a=l2-b-c
print(a*(CONSTANT**2)+b*(CONSTANT)+c)