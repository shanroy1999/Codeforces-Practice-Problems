"""n, d = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for i in range(len(l)-1):
    if(l[i+1]<=l[i]):
        l[i+1]+=d
        c+=1
print(c)"""

from math import ceil
n,d = map(int,input().split())
a=list(map(int,input().split()))
ans=0

for i in range(1,n):
    if a[i-1] >= a[i]:
        w = a[i-1] - a[i]
        a[i]+= ceil( (w+1)/d )*d
        ans+=ceil( (w+1)/d )
print(ans)
