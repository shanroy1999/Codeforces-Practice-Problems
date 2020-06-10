from fractions import Fraction

a, b = map(int, input().split())
m = max(a,b)
c = 0
l = [1,2,3,4,5,6]
for i in l:
    if(i>=m):
        c+=1
if(c%6!=0):
    print(Fraction(c, 6))
else:
    print(str(c//6)+"/1")
