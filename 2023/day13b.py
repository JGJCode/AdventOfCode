res=0
with open('day13.txt') as file:
    lines=file.readlines()
    graphs=[[]]
    for line in lines:
        line=line.rstrip()
        if line!='':
            graphs[-1].append(line)
        else:
            graphs.append([])
res=0
for graph in graphs:
    found=False
    for i in range(1,len(graph[0])):
        count=0
        for line in graph:
            one=line[:i]
            two=line[i:i+i][::-1]
            if len(one)!=len(two):
                break
            for j in range(len(one)):
                if one[j]!=two[j]:
                    count+=1
        else:
            if count==1:
                res+=i
                found=True
                break
    if found:
        continue
    for i in range(1,len(graph[0])):
        count=0
        for line in graph:
            one=line[len(line)-i:]
            two=line[len(line)-i-i:len(line)-i][::-1]
            if len(one)!=len(two):
                break
            for j in range(len(one)):
                if one[j]!=two[j]:
                    count+=1
        else:
            if count==1:
                res+=len(line)-i
                found=True
                break
    if found:
        continue
    for i in range(1,len(graph)):
        lp=i-1
        rp=i
        count=0
        while lp>=0 and rp<len(graph):
            for j in range(len(graph[lp])):
                if graph[lp][j]!=graph[rp][j]:
                    count+=1
            lp-=1
            rp+=1
        else:
            if count==1:
                res+=100*i
                break
print(res)

