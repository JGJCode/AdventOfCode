res=0
numbers=['','one','two','three','four','five','six','seven','eight','nine']
with open('day1.txt') as file:
    for line in file:
        num=''
        for i in range(len(line)):
            if line[i].isnumeric():
                num+=line[i]
            else:
                for j in range(1,len(numbers)):
                    if i+len(numbers[j])<len(line) and line[i:i+len(numbers[j])]==numbers[j]:
                        num+=str(j)
        res+=int(num[0]+num[-1])
print(res)