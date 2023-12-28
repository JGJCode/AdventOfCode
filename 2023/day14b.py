from copy import deepcopy
CONSTANT=10**9
grid=[]
with open('day14.txt') as file:
    for line in file:
        grid.append([x for x in line.rstrip()])

visited=[grid]
for _ in range(CONSTANT):
    mat=deepcopy(visited[-1])
    for col in range(len(mat[0])):
        next=0
        for row in range(len(mat)):
            if mat[row][col]=='#':
                next=row+1
            elif mat[row][col]=='O':
                mat[next][col],mat[row][col]=mat[row][col],mat[next][col]
                next+=1
    for row in range(len(mat)):
        next=0
        for col in range(len(mat[0])):
            if mat[row][col]=='#':
                next=col+1
            elif mat[row][col]=='O':
                mat[row][next],mat[row][col]=mat[row][col],mat[row][next]
                next+=1
    for col in range(len(mat[0])):
        next=len(mat)-1
        for row in range(len(mat)-1,-1,-1):
            if mat[row][col]=='#':
                next=row-1
            elif mat[row][col]=='O':
                mat[next][col],mat[row][col]=mat[row][col],mat[next][col]
                next-=1
    for row in range(len(mat)):
        next=len(mat[0])-1
        for col in range(len(mat[0])-1,-1,-1):
            if mat[row][col]=='#':
                next=col-1
            elif mat[row][col]=='O':
                mat[row][next],mat[row][col]=mat[row][col],mat[row][next]
                next-=1
    if mat in visited:
        print(f'REVISITED AT {_}, STARTED AT {visited.index(mat)}')
        index=visited.index(mat)+(CONSTANT-visited.index(mat))%(_-visited.index(mat)+1)
        res=visited[index]
        ans=0
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j]=='O':
                    ans+=len(res)-i
        print(ans)
        break
    visited.append(mat)
