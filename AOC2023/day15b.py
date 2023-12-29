import time
start=time.time()
def hash(string):
    res=0
    for char in string:
        res+=ord(char)
        res*=17
        res%=256
    return res
boxes=[[] for _ in range(256)]
seq=[]
with open('day15.txt') as file:
    for line in file:
        seq=line.rstrip().split(',')
for command in seq:
    if command[-1]=='-':
        charSequence=command[:len(command)-1]
        index=hash(charSequence)
        new=[]
        for i in range(len(boxes[index])):
            if boxes[index][i][0]!=charSequence:
                new.append(boxes[index][i])
        boxes[index]=new
    else:
        charSequence,focal_length=command.split('=')
        index=hash(charSequence)
        for i in range(len(boxes[index])):
            if boxes[index][i][0]==charSequence:
                boxes[index][i][1]=focal_length
                break
        else:
            boxes[index].append([charSequence,focal_length])
res=0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        res+=(i+1)*(j+1)*int(boxes[i][j][1])
print(res)
print(time.time()-start)