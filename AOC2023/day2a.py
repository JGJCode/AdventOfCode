res=0
r=12
g=13
b=14
with open('day2.txt') as file:
    for line in file:
        gameID=int(line[5:line.index(':')])
        line=line[line.index(':')+2:]
        line=line.split(';')
        flag=False
        print(line)
        for group in line:
            colors=group.split(',')
            for color in colors:
                number=""
                for i in range(len(color)):
                    if color[i].isalpha():
                        if color[i]=='b' and int(number)>b:
                            flag=True
                        elif color[i]=='g' and int(number)>g:
                            flag=True
                        elif color[i]=='r' and int(number)>r:
                            flag=True
                        break
                    else:
                        number+=color[i]
        if not flag:
            res+=gameID
print(res)

