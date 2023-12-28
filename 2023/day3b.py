grid=[]
with open('day3.txt') as file:
    for line in file:
        grid.append(line)
for i in range(len(grid)-1):
    grid[i]=grid[i][:len(grid[i])-1]
res=0
DIRECTIONS=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='*':
            visited=set()
            numbers=[]
            for dr,dc in DIRECTIONS:
                if (not 0<=i+dr<len(grid)) or (not 0<=j+dc<len(grid[0])) or (not grid[i+dr][j+dc].isnumeric()) or (i+dr,j+dc) in visited:
                    continue
                number=''
                lp=j+dc
                while lp>=0 and grid[i+dr][lp].isnumeric():
                    visited.add((i+dr,lp))
                    number=grid[i+dr][lp]+number
                    lp-=1
                rp=j+dc+1
                while rp<len(grid[i]) and grid[i+dr][rp].isnumeric():
                    visited.add((i+dr,rp))
                    number+=grid[i+dr][rp]
                    rp+=1
                numbers.append(number)
            if len(numbers)==2:
                res+=int(numbers[0])*int(numbers[1])
            print(numbers)
print(res)