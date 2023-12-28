from collections import deque,defaultdict
outputs=defaultdict(list)
inputs=defaultdict(list) #False->Low, True->High
with open('day20.txt') as file:
    for line in file:
        input,output=line.rstrip().split('->')
        items=[False]+list(map(lambda x:x[1:],output.split(',')))
        outputs[input[:len(input)-1]]=items
        for item in items:
            inputs[item].append([input[1:len(input)-1],False])
low=0
high=0
for i in range(1000):
    q=deque([('broadcaster',False)])
    while q:
        module,pulse=q.popleft()
        if module=='broadcaster':
            low+=1
            for output in outputs['broadcaster'][1:]:
                low+=1
                if '%'+output in outputs:
                    q.append(('%'+output,False))
                else:
                    q.append(('&'+output,False))
        elif module[0]=='%':
            if pulse:
                continue
            highPulse=False
            if not outputs[module][0]:
                outputs[module][0]=True
                highPulse=True
            else:
                outputs[module][0]=False
            for output in outputs[module][1:]:
                if highPulse:
                    high+=1
                else:
                    low+=1
                if '&'+output in outputs:
                    for j in range(len(inputs[output])):
                        if inputs[output][j][0]==module[1:]:
                            inputs[output][j][-1]=highPulse
                            break
                    q.append(('&'+output,highPulse))
                else:
                    q.append(('%'+output,highPulse))
        else:
            lowPulse=True
            for input in inputs[module[1:]]:
                if not input[1]:
                    lowPulse=False
                    break
            for output in outputs[module][1:]:
                if lowPulse:
                    low+=1
                else:
                    high+=1
                if '%'+output in outputs:
                    q.append(('%'+output,not lowPulse))
                else:
                    for j in range(len(inputs[output])):
                        if inputs[output][j][0]==module[1:]:
                            inputs[output][j][-1]=not lowPulse
                            break
                    q.append(('&'+output,not lowPulse))
print(low*high)