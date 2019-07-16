num=int(input())
lis=[]
for i in range(num):
    h=input()
    s=list(map(int,h.split()))
    lis=lis+s
lis.sort()
for i in lis:
    print(i,end=" ")
