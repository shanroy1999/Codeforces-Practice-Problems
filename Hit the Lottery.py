a = int(input())
count=0
while(a!=0):
    if(a>=100):
        count+=a//100
        a=a%100
    elif(20<=a<100):
        count+=a//20
        a=a%20
    elif(10<=a<20):
        count+=a//10
        a=a%10
    elif(5<=a<10):
        count+=a//5
        a=a%5
    else:
        count+=a//1
        a=a%1
print(count)
