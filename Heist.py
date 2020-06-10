n = int(input())
l = list(map(int, input().split()))

mn = min(l)
print(max(l) - (mn+n-1))
