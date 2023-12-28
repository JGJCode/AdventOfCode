from collections import Counter
biddings={}
hands=[]
with open('day7.txt') as file:
    for line in file:
        hand,money=line.split()
        hands.append(hand)
        biddings[hand]=int(money)
def getStrength(hand) -> int:
    counter=Counter(hand)
    if 'J' in counter:
        maxkey=''
        for key in counter:
            if key!='J' and counter[key]>counter[maxkey]:
                maxkey=key
        counter[maxkey]+=counter['J']
        counter.pop('J')
    counts=sorted(counter.values())
    if len(counts)==1:
        return 7
    elif len(counts)==2:
        return 6 if counts[-1]==4 else 5
    elif len(counts)==3:
        return 4 if counts[-1]==3 else 3
    else:
        return 2 if len(counts)==4 else 1
cards={'J':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'Q':12,'K':13,'A':14}
hands.sort(key=lambda hand:(getStrength(hand),cards[hand[0]],cards[hand[1]],cards[hand[2]],cards[hand[3]],cards[hand[4]]))
res=0
for i in range(len(hands)):
    res+=(i+1)*biddings[hands[i]]
print(res)