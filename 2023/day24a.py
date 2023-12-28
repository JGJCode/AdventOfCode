import numpy as np
LOWER=200000000000000
UPPER=400000000000000
stones=[]
with open('day24.txt') as file:
    for line in file:
        pos,vel=line.split('@')
        stones.append([list(map(int,pos.split(','))),list(map(int,vel.split(',')))])
res=0
for i in range(len(stones)):
    p1=stones[i][0]
    v1=stones[i][1]
    for j in range(i+1,len(stones)):
        p2=stones[j][0]
        v2=stones[j][1]
        if v1[1]/v1[0]==v2[1]/v2[0]: #if lines are parallel
            continue
        eq1right=p2[0]-p1[0]
        eq2right=p2[1]-p1[1]
        matrix=np.array([[v1[0],-v2[0]],
                     [v1[1],-v2[1]]])
        b=np.array([eq1right,eq2right])
        x,y=np.dot(np.linalg.inv(matrix),b)
        if x<0 or y<0:
            continue
        intersectionX=p1[0]+(v1[0]*x)
        intersectionY=p1[1]+(v1[1]*x)
        if LOWER<=intersectionX<=UPPER and LOWER<=intersectionY<=UPPER:
            res+=1
        
print(res)
