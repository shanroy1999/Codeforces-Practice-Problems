a = input()
l = list(map(str, input().split()))
count=0
for i in l:
    if(i[0]==a[0] or i[1]==a[1]):
        count+=1
    else:
        pass
if(count>0):
    print("YES")
else:
    print("NO")
