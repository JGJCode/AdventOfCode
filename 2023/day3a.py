grid=[]
with open('day3.txt') as file:
    for line in file:
        grid.append(line)
for i in range(len(grid)-1):
    grid[i]=grid[i][:len(grid[i])-1]
res=0
DIRECTIONS=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
for i in range(len(grid)):
    col=0
    while col<len(grid[i]):
        if grid[i][col].isnumeric():
            add=False
            number=""
            temp=col
            while temp<len(grid[i]) and grid[i][temp].isnumeric():
                number+=grid[i][temp]
                if not add:
                    for dr,dc in DIRECTIONS:
                        if 0<=i+dr<len(grid) and 0<=temp+dc<len(grid[i+dr]) and grid[i+dr][temp+dc]!='.' and (not grid[i+dr][temp+dc].isnumeric()):
                            add=True
                            break
                temp+=1
            else:
                if add:
                    res+=int(number)
                col=temp-1
        col+=1
print(res)