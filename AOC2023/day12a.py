from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(remainingString,remainingLengths): 
    if not remainingString:
        return int(not remainingLengths)
    if not remainingLengths:
        return int('#' not in remainingString)
    if remainingLengths[0]>len(remainingString):
        return 0
    if remainingLengths[0]<=len(remainingString)-1 and remainingString[remainingLengths[0]]=='#':
        if remainingString[0]=='#':
            return 0
    res=0
    if remainingString[0]=='#':
        for i in range(remainingLengths[0]):
            if remainingString[i]=='.':
                return 0
        else:
            for j in range(i+2,len(remainingString)):
                if remainingString[j]=='#' or remainingString[j]=='?':
                    res+=dfs(remainingString[j:],remainingLengths[1:])
                    break
            else:
                res+=dfs("",remainingLengths[1:])
    else:
        for i in range(remainingLengths[0]):
            if remainingString[i]=='.':
                break
        else:
            if remainingLengths[0]<len(remainingString):
                if remainingString[remainingLengths[0]]!='#':
                    for j in range(remainingLengths[0]+1,len(remainingString)):
                        if remainingString[j]=='#' or remainingString[j]=='?':
                            res+=dfs(remainingString[j:],remainingLengths[1:])
                            break
                    else:
                        res+=dfs("",remainingLengths[1:])
            else:
                res+=dfs("",remainingLengths[1:])
        for i in range(1,len(remainingString)):
            if remainingString[i]=='#' or remainingString[i]=='?':
                res+=dfs(remainingString[i:],remainingLengths)
                break
    return res
ans=0
with open('day12.txt') as file:
    for line in file:
        pattern,counts=line.split()
        counts=tuple(map(int,counts.split(',')))
        ans+=dfs(pattern,counts)
print(ans)
