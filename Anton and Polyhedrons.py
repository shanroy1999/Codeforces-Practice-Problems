t = int(input())
count = 0
for i in range(t):
    s = input()

    if('Icosa' in s):
        count+=20
    elif('Cube' in s):
        count+=6
    elif('Tetra' in s):
        count+=4
    elif('Dodeca' in s):
        count+=12
    elif('Octa' in s):
        count+=8

print(count)
