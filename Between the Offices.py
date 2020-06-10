n = int(input())
a = input()
SF = 0
FS = 0
for i in range(len(a)-1):
    if(a[i]=='S' and a[i+1]=='F'):
        SF+=1
    elif(a[i]=='F' and a[i+1]=='S'):
        FS+=1
if(SF>FS):
    print("YES")
else:
    print("NO")
