from collections import defaultdict
workflows=defaultdict(list)
def check(variable,condition):
    number=int(condition[2:condition.index(':')])
    if condition[1]=='<':
        if variable<number:
            return True
    elif condition[1]=='>':
        if variable>number:
            return True
    return False
def dfs(wf,x,m,a,s):
    last=workflows[wf][-1]
    for i in range(len(workflows[wf])-1):
        condition=workflows[wf][i]
        if condition[0]=='x':
            if check(x,condition):
                if condition[condition.index(':')+1:]=='A':
                    return True
                elif condition[condition.index(':')+1:]=='R':
                    return False
                return dfs(condition[condition.index(':')+1:],x,m,a,s)
        elif condition[0]=='m':
            if check(m,condition):
                if condition[condition.index(':')+1:]=='A':
                    return True
                elif condition[condition.index(':')+1:]=='R':
                    return False
                return dfs(condition[condition.index(':')+1:],x,m,a,s)
        elif condition[0]=='a':
            if check(a,condition):
                if condition[condition.index(':')+1:]=='A':
                    return True
                elif condition[condition.index(':')+1:]=='R':
                    return False
                return dfs(condition[condition.index(':')+1:],x,m,a,s)
        elif condition[0]=='s':
            if check(s,condition):
                if condition[condition.index(':')+1:]=='A':
                    return True
                elif condition[condition.index(':')+1:]=='R':
                    return False
                return dfs(condition[condition.index(':')+1:],x,m,a,s)
    else:
        if last=='A':
            return True
        elif last=='R':
            return False
        return dfs(last,x,m,a,s)
        
res=0
with open('day19.txt') as file:
    for line in file:
        if line[0].isalpha():
            name=line[:line.index('{')]
            conditions=line[line.index('{')+1:line.index('}')].split(',')
            workflows[name]=conditions
        elif line[0]=='{':
            numbers=line[1:line.index('}')].split(',')
            xmas=[]
            for number in numbers:
                xmas.append(int(number[2:]))
            if dfs('in',xmas[0],xmas[1],xmas[2],xmas[3]):
                res+=sum(xmas)
print(res)
