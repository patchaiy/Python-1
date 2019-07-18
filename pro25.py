num=int(input())
lis=list(map(int,input().split()))
lis2=[]
count=0
for i in range(num-1):
  if lis[i]>=lis[i+1]:
    count+=1
  else:
    count+=1
    lis2.append(count)
    count=0
m=max(lis2)
print(m)
