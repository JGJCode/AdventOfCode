cards=[]
with open('day4.txt') as file:
    for line in file:
        l=line[line.index(':')+2:]
        cards.append(l.split('|'))
res=0
for card in cards:
    winning=set()
    w=card[0].split()
    for num in w:
        if num.isnumeric():
            winning.add(num)
    nums=card[1].split()
    count=0
    for num in nums:
        if num.isnumeric() and num in winning:
            count+=1
    if count>0:
        res+=2**(count-1)
print(res)