t = int(input())
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    min_a = abs(a-b)
    max_a = a+b
    min_c = abs(c-d)
    max_c = c+d
    if(n*max_a >= min_c and n*min_a<=max_c):
        print("Yes")
    else:
        print("No")
