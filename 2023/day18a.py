rows=[]
cols=[]
count=0
with open('day18.txt') as file:
    for line in file:
        dir,mag,color=line.rstrip().split()
        mag=int(mag)
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

