n,m = map(int, input().split())
a = input().split()
b = input().split()
for _ in range(int(input())):
    num = int(input())
    x = num % n - 1
    y = num % m - 1
    s = a[x] + b[y]
    print(s)
