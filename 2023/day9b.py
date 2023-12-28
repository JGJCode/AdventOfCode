res=0
with open('day9.txt') as file:
    for line in file:
        differences=[list(map(int,line.split()))]
        allZero=False
        while not allZero:
            new=[]
            allZero=True
            for i in range(1,len(differences[-1])):
                new.append(differences[-1][i]-differences[-1][i-1])
                if new[-1]!=0:
                    allZero=False
            differences.append(new)
        diff=0
        for i in range(len(differences)-2,-1,-1):
            diff=differences[i][0]-diff
            differences[i].insert(0,diff)
        res+=differences[0][0]
print(res)