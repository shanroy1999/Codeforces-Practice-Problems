t = int(input())
a = list(map(int, input().split()))
index = []
f = []
for i in a:
    index.append(a.index(i)+1)

for i in index:
    for j in a:
        if(i==j):
            f.append(a.index(i)+1)

for i in f:
    print(i, end=' ')
