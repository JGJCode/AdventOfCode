import heapq
from collections import defaultdict
grid=[]
with open('day17.txt') as file:
    for line in file:
        grid.append(list(map(int,line.rstrip())))
heap=[(grid[0][1],0,1,0,1,1),(grid[1][0],1,0,1,0,1)] #heatloss,row,col,dx,dy,number of cells straight
heapq.heapify(heap)

heatMap=defaultdict(lambda: float('inf'))
heatMap[(0,1,0,1,1)]=grid[0][1]
heatMap[(1,0,1,0,1)]=grid[1][0]
while heap:
    heatloss,r,c,dx,dy,numstraight=heapq.heappop(heap)
    if r==len(grid)-1 and c==len(grid[0])-1:
        print(heatloss)
        exit()
    directions={(0,1),(0,-1),(1,0),(-1,0)}
    if numstraight==3:
        directions.remove((dx,dy))
    directions.remove((dx*-1,dy*-1))
    for dr,dc in directions:
        if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]):
            if dr==dx and dc==dy:
                if heatloss+grid[r+dr][c+dc]<heatMap[(r+dr,c+dc,dr,dc,numstraight+1)]:
                    heatMap[(r+dr,c+dc,dr,dc,numstraight+1)]=heatloss+grid[r+dr][c+dc]
                    heapq.heappush(heap,(heatloss+grid[r+dr][c+dc],r+dr,c+dc,dr,dc,numstraight+1))
            elif heatloss+grid[r+dr][c+dc]<heatMap[(r+dr,c+dc,dr,dc,1)]:
                heatMap[(r+dr,c+dc,dr,dc,1)]=heatloss+grid[r+dr][c+dc]
                heapq.heappush(heap,(heatloss+grid[r+dr][c+dc],r+dr,c+dc,dr,dc,1))