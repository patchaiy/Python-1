num=int(input())
lis=[]
for i in range(num):
    a=input()
    lis.append(a)
first=lis[0]
second=lis[1]
ans=[]
for i in range(len(first)):
    if first[i]==second[i]:
        ans.append(first[i])
    else:
        break
ansstr=""
for i in range(len(ans)):
    ansstr=ansstr+ans[i]
newlis=[]
tempstr=""
if num>2:
    for i in range(2,num):
        temp=[]
        for i in range(len(lis[i])):
            if lis[i]==ansstr[i]:
                temp.append()
            else:
                break
        if temp!=[]:
            tempstr=str(temp)
            newlis.append(tempstr)
newlis.append(ansstr)
print(newlis[0])
    
