n=int(input())
lis=[]
for i in range(n):
    lis.append(int(input()))
set1=set(lis)
count1=1
ans=[]
for i in set1:
    count1=lis.count(i)
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
    
