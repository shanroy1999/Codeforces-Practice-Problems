"""n, k = map(int, input().split())
o = []
e = []
for i in range(1,n+1):
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
l = o+e
print(l[k-1])"""

import math
n,k=map(int,input().split())
if k<=n//2:
    print(2*k-1)
else:
    i=k-math.ceil(n/2)
    if i!=0:
        print(2*i)
    else:
        print(n)
