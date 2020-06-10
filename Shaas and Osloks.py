n = int(input())
l = list(map(int, input().split()))
m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    if(n!=1):
        if(1<a<n):
            l[a-2] += l[a-1]-(l[a-1]-b+1)
            l[a] += l[a-1]-b
            l[a-1] = 0
        elif(a==1):
            l[a] += l[a-1]-b
            l[a-1]=0
        elif(a==n):
            l[a-2]+=l[a-1]-(l[a-1]-b+1)
            l[a-1]=0
    elif(n==1):
        l[a-1]=0

for i in l:
    print(i)
