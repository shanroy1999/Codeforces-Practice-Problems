n = int(input())
l = []
s = 0
for i in range(n):
    a = list(map(int, input().split()))
    l.append(a)

for i in range(len(l)):
    for j in range(len(l[i])):
        if(i==j):
            s+=l[i][j]
        elif((i+j)==n-1):
            s+=l[i][j]
        elif(j==(n-1)/2):
            s+=l[i][j]
        elif(i==(n-1)/2):
            s+=l[i][j]
print(s)
