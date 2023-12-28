from collections import defaultdict
workflows=defaultdict(list)
with open('day19.txt') as file:
    for line in file:
        if line[0].isalpha():
            name=line[:line.index('{')]
            conditions=line[line.index('{')+1:line.index('}')].split(',')
            workflows[name]=conditions
        else:
            break
res=0
def dfs(wf,lastXmax,lastMmax,lastAmax,lastSmax,lastXmin,lastMmin,lastAmin,lastSmin):
    global res
    if wf=='A':
        res+=(lastXmax-lastXmin+1)*(lastMmax-lastMmin+1)*(lastAmax-lastAmin+1)*(lastSmax-lastSmin+1)
        return
    elif wf=='R':
        return
    last=workflows[wf][-1]
    for i in range(len(workflows[wf])-1):
        condition=workflows[wf][i]
        variable=condition[0]
        number=int(condition[2:condition.index(':')])
        destination=condition[condition.index(':')+1:]
        if variable=='x' and condition[1]=='>':
            dfs(destination,lastXmax,lastMmax,lastAmax,lastSmax,max(lastXmin,number+1),lastMmin,lastAmin,lastSmin)
            lastXmax=min(lastXmax,number)
        elif variable=='x' and condition[1]=='<':
            dfs(destination,min(lastXmax,number-1),lastMmax,lastAmax,lastSmax,lastXmin,lastMmin,lastAmin,lastSmin)
            lastXmin=max(lastXmin,number)
        elif variable=='m' and condition[1]=='>':
            dfs(destination,lastXmax,lastMmax,lastAmax,lastSmax,lastXmin,max(lastMmin,number+1),lastAmin,lastSmin)
            lastMmax=min(lastMmax,number)
        elif variable=='m' and condition[1]=='<':
            dfs(destination,lastXmax,min(lastMmax,number-1),lastAmax,lastSmax,lastXmin,lastMmin,lastAmin,lastSmin)
            lastMmin=max(lastMmin,number)
        elif variable=='a' and condition[1]=='>':
            dfs(destination,lastXmax,lastMmax,lastAmax,lastSmax,lastXmin,lastMmin,max(lastAmin,number+1),lastSmin)
            lastAmax=min(lastAmax,number)
        elif variable=='a' and condition[1]=='<':
            dfs(destination,lastXmax,lastMmax,min(lastAmax,number-1),lastSmax,lastXmin,lastMmin,lastAmin,lastSmin)
            lastAmin=max(lastAmin,number)
        elif variable=='s' and condition[1]=='>':
            dfs(destination,lastXmax,lastMmax,lastAmax,lastSmax,lastXmin,lastMmin,lastAmin,max(lastSmin,number+1))
            lastSmax=min(lastSmax,number)
        elif variable=='s' and condition[1]=='<':
            dfs(destination,lastXmax,lastMmax,lastAmax,min(lastSmax,number-1),lastXmin,lastMmin,lastAmin,lastSmin)
            lastSmin=max(lastSmin,number)
    else:
        dfs(last,lastXmax,lastMmax,lastAmax,lastSmax,lastXmin,lastMmin,lastAmin,lastSmin)
dfs('in',4000,4000,4000,4000,1,1,1,1)
print(res)
