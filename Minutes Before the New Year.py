t = int(input())
for i in range(t):
    h,m = map(int, input().split())
    t = (24-h)*60 - m
    print(t)
