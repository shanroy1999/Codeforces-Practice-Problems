a1,a2,a3,a4 = map(int, input().split())
a = input()
sum=0
c1,c2,c3,c4 = 0,0,0,0
for i in a:
    if(i=='1'):
        c1+=1
    elif(i=='2'):
        c2+=1
    elif(i=='3'):
        c3+=1
    elif(i=='4'):
        c4+=1
sum+=c1*a1+c2*a2+c3*a3+c4*a4
print(sum)
