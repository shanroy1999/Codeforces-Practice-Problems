n = int(input())
l = 0
count=0
for i in range(1,n):
    if(n%i==0):
        count+=1
print(count)
