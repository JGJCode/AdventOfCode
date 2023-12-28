grid=[]
with open('day11.txt') as file:
    for line in file:
        grid.append(list(line.rstrip()))
tar=['.']*len(grid[0])
emptyRows=[]
for i in range(len(grid)):
    if grid[i]==tar:
        emptyRows.append(i)
emptyCols=[]
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if grid[j][i]=='#':
            break
    else:
        emptyCols.append(i)
galaxies=[]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=='#':
            galaxies.append([i,j])
res=0
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        res+=abs(galaxies[i][0]-galaxies[j][0])+abs(galaxies[i][1]-galaxies[j][1])
        for row in emptyRows:
            if galaxies[i][0]<row<galaxies[j][0] or galaxies[j][0]<row<galaxies[i][0]:
                res+=999_999
        for col in emptyCols:
            if galaxies[i][1]<col<galaxies[j][1] or galaxies[j][1]<col<galaxies[i][1]:
                res+=999_999
print(res)
