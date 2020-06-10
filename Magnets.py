a=''
for i in range(int(input())):
    a+=input()
print(a.count('11')+a.count('00')+1)
