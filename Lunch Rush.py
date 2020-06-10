n, k = map(int, input().split())
l = []
for i in range(n):
    f, t = map(int, input().split())
    l.append((f,t))

l2 = []
for i in l:
    if(i[1]<=k):
        l2.append(i[0])
    else:
        l2.append(i[0]-(i[1]-k))
print(max(l2))
