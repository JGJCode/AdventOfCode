res=0
with open('day15.txt') as file:
    for line in file:
        strings=line.rstrip().split(',')
        for string in strings:
            temp=0
            for char in string:
                temp+=ord(char)
                temp*=17
                temp%=256
            res+=temp
print(res)