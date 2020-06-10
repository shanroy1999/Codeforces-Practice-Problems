n = int(input())
s = input()
l = []
for i in s:
    if(i=='n'):
        l.append(1)
    elif(i=='z'):
        l.append(0)
l = sorted(l, reverse=True)
for i in l:
    print(i, end=' ')
