t = int(input())
s = input()
l = [i for i in s]
c=0
n = len(l)
i = 1
while(i<n):
    if(l[i]==l[i-1]):
        del l[i]
        n-=1
    else:
        i+=1
print(len(s)-len(l))
