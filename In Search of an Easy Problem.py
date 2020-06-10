a = int(input())
b = list(map(int, input().split()))
if(sum(b)>=1):
    print("HARD")
else:
    print("EASY")
