n, m = map(int, input().split())
prev = -100
for _ in range(n):
    se = list(set(input()))

    if len(se) != 1:
        print('NO')
        exit()

    elif se[0] == prev:
        print('NO')
        exit()

    else:
        prev = se[0]

print('YES')
