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
res=float('inf')
next={'seeds':'soil','soil':'fertilizer','fertilizer':'water','water':'light','light':'temperature','temperature':'humidity','humidity':'location','location':'final'}
data={'soil':soil,'fertilizer':fertilizer,'water':water,'light':light,'temperature':temperature,'humidity':humidity,'location':location}
def dfs(start:int,end:int,name:str):
    global res
    if name=='final':
        res=min(start,res)
        return
    for line in data[name]:
        if start>=line[1]+line[2] or end<line[1]:
            continue
        if end==line[1]:
            dfs(line[0],line[0],next[name])
            continue
        startDiff=endDiff=0
        if start>=line[1]:
            startDiff=start-line[1]
        if end>=line[1]+line[2]:
            endDiff=line[2]-1
        else:
            endDiff=end-line[1]
        dfs(line[0]+startDiff,line[0]+endDiff,next[name])
seeds=[[194657215, 187012821],
       [1093203236, 6077151],
       [44187305, 148722449],
       [2959577030, 152281079],
       [3400626717, 198691716],
       [1333399202, 287624830],
       [2657325069, 35258407],
       [1913289352, 410917164],
       [1005856673, 850939],
       [839895010, 162018909]]
for seed in seeds:
    dfs(seed[0],seed[0]+seed[1]-1,'soil')
print(res)
