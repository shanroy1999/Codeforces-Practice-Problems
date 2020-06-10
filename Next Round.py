a, b = map(int, input().split())
l = list(map(int, input().split()))
s = l[b-1]
count = 0
for i in l:
    if(i>0):
        if(i>=s):
            count+=1
print(count)
