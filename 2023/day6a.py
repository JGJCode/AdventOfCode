time=[]
distance=[]
with open('day6.txt') as file:
    lines=file.readlines()
    time=list(map(int,lines[0].split()))
    distance=list(map(int,lines[1].split()))
res=1
#-x(x-time)=-x^2+time*x-> max=-b/2a=-time/-2=time/2
for i in range(len(time)):
    lp=0
    rp=time[i]//2
    while lp<=rp:
        mid=(lp+rp)//2
        if (time[i]-mid)*mid>distance[i]:
            rp=mid-1
        else:
            lp=mid+1
    left=lp
    lp=time[i]//2
    rp=time[i]
    while lp<=rp:
        mid=(lp+rp)//2
        if (time[i]-mid)*mid>distance[i]:
            lp=mid+1
        else:
            rp=mid-1
    res*=(rp-left+1)
print(res)