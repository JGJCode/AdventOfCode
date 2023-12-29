grid=[]
with open('day14.txt', 'r') as file:
    for line in file:
        grid.append(line.rstrip())
rocks={i:0 for i in range(len(grid[0]))}
res=0
for col in range(len(grid[0])):
    for row in range(len(grid)):
        if grid[row][col]=='#':
            rocks[col]=row+1
        elif grid[row][col]=='O':
            res+=len(grid)-rocks[col]
            rocks[col]+=1
print(res)