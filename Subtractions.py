t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    count=0
    while a>0 and b>0:
        if a>=b:
            count+=(a//b)
            a=a-((a//b)*b)
        else:
            count+=(b//a)
            b=b-((b//a)*a)
    print(count)
