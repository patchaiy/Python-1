nm=input()
lis1=list(map(int,input().split()))
maximum=0
i=0
while(i<len(lis1)-1):
    count=0
    while(i<len(lis1)-1 and lis1[i]<lis1[i+1]):
        count+=1
        i+=1
    if(count>maximum):
        maximum=count
    i+=1
print(maximum+1)
