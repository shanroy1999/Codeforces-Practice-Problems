t =list(map(int,input().split()))
t.sort()
if t[0]+t[1]>t[2] or t[1]+t[2]>t[3]:
    print('TRIANGLE')
elif t[0]+t[1]==t[2] or t[1]+t[2]==t[3]:
    print('SEGMENT')
else:
    print('IMPOSSIBLE')
