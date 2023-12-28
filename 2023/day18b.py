def hex2dec(string):
    res=0
    place=1
    letters={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    for i in range(len(string)-1,-1,-1):
        multiplier=letters[string[i]] if string[i] in letters else int(string[i])
        res+=place*multiplier
        place*=16
    return res
rows=[]
cols=[]
count=0
dirMap={0:'R',1:'D',2:'L',3:'U'}
with open('day18.txt') as file:
    for line in file:
        _,__,color=line.rstrip().split()
        mag=hex2dec(color[2:len(color)-2])
        dir=dirMap[int(color[-2])]
        count+=mag
        if dir=='R':
            rows.append(rows[-1] if rows else 0)
            cols.append(cols[-1]+mag if cols else mag)
        elif dir=='L':
            rows.append(rows[-1] if rows else 0)
            cols.append(cols[-1]-mag if cols else -mag)
        elif dir=='U':
            rows.append(rows[-1]-mag if rows else -mag)
            cols.append(cols[-1] if cols else 0)
        elif dir=='D':
            rows.append(rows[-1]+mag if rows else mag)
            cols.append(cols[-1] if cols else 0)
xSum=cols[-1]*rows[0]
for i in range(len(cols)-1):
    xSum+=cols[i]*rows[i+1]
ySum=rows[-1]*cols[0]
for i in range(len(cols)-1):
    ySum+=rows[i]*cols[i+1]
area=int(0.5*abs(xSum-ySum))
interior=area+1-(count)/2
print(count+int(interior))

