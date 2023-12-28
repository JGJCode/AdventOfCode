res=0
with open('day2.txt') as file:
    for line in file:
        r=g=b=0
        line=line[line.index(':')+2:]
        line=line.split(';')
        print(line)
        for group in line:
            colors=group.split(',')
            for color in colors:
                number=""
                for i in range(len(color)):
                    if color[i].isalpha():
                        if color[i]=='b' and int(number)>b:
                            b=int(number)
                        elif color[i]=='g' and int(number)>g:
                            g=int(number)
                        elif color[i]=='r' and int(number)>r:
                            r=int(number)
                        break
                    else:
                        number+=color[i]
        res+=(r*g*b)
print(res)