res=0
with open('day1.txt') as file:
    for line in file:
        num=""
        for char in line:
            if char.isnumeric():
                num+=char
        res+=int(num[0]+num[-1])
print(res)