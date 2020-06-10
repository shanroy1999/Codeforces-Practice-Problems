t = int(input())
l = list(map(int, input().split()))
chest = 0
bicep = 0
back = 0

for i in range(1, len(l)+1):
    if(i%3==1):
        chest+=l[i-1]
    elif(i%3==2):
        bicep+=l[i-1]
    else:
        back+=l[i-1]

m = max(chest, bicep, back)
if(m==back):
    print("back")
elif(m==chest):
    print("chest")
else:
    print("biceps")
