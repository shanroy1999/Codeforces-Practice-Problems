t = int(input())
s = int(input())
v = int(input())
j = int(input())
e = int(input())
f = int(input())

a1 = min(t,j)
b1 = min(s, v, j-a1)
b2 = min(s, v, j)
a2 = min(t, j-b2)

if(e<=f):
    if(b1 >= b2):
        print(b1*f+a1*e)
    else:
        print(b2*f+a2*e)
else:
    if(b1 >= b2):
        print(b2*f+a2*e)
    else:
        print(b1*f+a1*e)
