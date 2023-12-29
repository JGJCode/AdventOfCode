time=0
distance=0
with open('day6.txt') as file:
    lines=file.readlines()
    time=int(''.join(lines[0].split()))
    distance=int(''.join(lines[1].split()))
lp=0
rp=time//2
while lp<=rp:
    mid=(lp+rp)//2
    if (time-mid)*mid>distance:
        rp=mid-1
    else:
        lp=mid+1
left=lp
lp=time//2
rp=time
while lp<=rp: #find first point on right of the max where toy distance does not beat record
    mid=(lp+rp)//2
    if (time-mid)*mid>distance:
        lp=mid+1
    else:
        rp=mid-1
print(rp-left+1)
