t = int(input())
l = []
c = 0
for i in range(t):
    h, a = map(int, input().split())
    l.append((h, a))
for i in l:
    for j in l:
        if(j!=i):
            if(i[0]==j[1]):
                c+=1
print(c)
