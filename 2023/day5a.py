index=-1
seeds=[]
soil=[]
fertilizer=[]
water=[]
light=[]
temperature=[]
humidity=[]
location=[]
with open('day5.txt') as file:
    for line in file:
        if line[0].isalpha():
            index+=1
            continue
        t=list(map(int,line.split()))
        if index==0:
            seeds.append(t)
        elif index==1:
            soil.append(t)
        elif index==2:
            fertilizer.append(t)
        elif index==3:
            water.append(t)
        elif index==4:
            light.append(t)
        elif index==5:
            temperature.append(t)
        elif index==6:
            humidity.append(t)
        elif index==7:
            location.append(t)
seeds=seeds[0]
res=float('inf')
next={'seeds':'soil','soil':'fertilizer','fertilizer':'water','water':'light','light':'temperature','temperature':'humidity','humidity':'location'}
data={'soil':soil,'fertilizer':fertilizer,'water':water,'light':light,'temperature':temperature,'humidity':humidity,'location':location}
def dfs(source:int,name:str):
    global res
    destination=source
    for line in data[name]:
        if line[1]<=source<line[1]+line[2]:
            diff=source-line[1]
            destination=line[0]+diff
            break
    if name=='location':
        res=min(destination,res)
        return
    dfs(destination,next[name])
for seed in seeds:
    dfs(seed,'soil')
print(res)
