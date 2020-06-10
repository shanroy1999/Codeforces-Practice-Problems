t = int(input())
a = list(map(int, input().split()))
s = sum(a)
mean = s/t

print("{:.12f}".format(mean))
