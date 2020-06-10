for _ in range(int(input())):
    a,b = map(int,input().split())
    c,d = map(int,input().split())

    flag=0
    if a==c and b+d==a:
        flag=1

    if a==d and b+c==a:
        flag=1

    if b==c and a+d==b:
        flag=1

    if b==d and a+c==b:
        flag=1

    if flag==1:
        print('Yes')
    else:
        print('No')
