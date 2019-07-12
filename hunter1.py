num=int(input())
lis1=list(map(int,input().split()))
set1=set(lis1)
count1=1
ans=[]
for i in set1:
    count1=lis1.count(i)
    if count1>1:
        ans.append(i)
    else:
        pass
if len(ans)==1:
    print(ans)
elif len(ans)>1:
    print(ans.sort)
else:
    print("unique")
    
