a = list(map(int, input().split()))
m = max(a)
b = []
for i in a:
    if(i<m):
        b.append(m-i)
    else:
        pass
for i in b:
    print(i, end=' ')
