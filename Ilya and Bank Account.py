n=int(input())
if n==abs(n):
    print(n)
else:
    n1=int(str(n)[:-1])
    n2=int(str(n)[:-2]+str(n)[-1])
    if n1>n2:
        print(n1)
    else:
        print(n2)
