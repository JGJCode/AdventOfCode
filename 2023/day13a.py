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
        for line in graph:
            if line[:i]!=line[i:i+i][::-1]:
                break
        else:
            res+=i
            found=True
            break
    if found:
        continue
    for i in range(1,len(graph[0])):
        for line in graph:
            if line[len(line)-i:]!=line[len(line)-i-i:len(line)-i][::-1]:
                break
        else:
            res+=len(line)-i
            found=True
            break
    if found:
        continue
    for i in range(1,len(graph)):
        lp=i-1
        rp=i
        while lp>=0 and rp<len(graph):
            if graph[lp]!=graph[rp]:
                break
            lp-=1
            rp+=1
        else:
            res+=100*i
            break
print(res)
