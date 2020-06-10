n = int(input())
for i in range(n):
    a = int(input())
    l = list(map(int, input().split()))
    l = set(l)

    print(len(l))
