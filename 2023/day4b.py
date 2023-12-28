cards=[]
with open('day4.txt') as file:
    for line in file:
        l=line[line.index(':')+2:]
        cards.append(l.split('|'))
copies={x:1 for x in range(202)}
for i in range(len(cards)):
    winning=set()
    for num in cards[i][0].split():
        if num.isnumeric():
            winning.add(num)
    count=0
    for num in cards[i][1].split():
        if num.isnumeric() and num in winning:
            count+=1
    for j in range(i+1,min(i+count+1,len(cards))):
        copies[j]+=copies[i]
print(sum(copies.values()))