num=input()
lis=[]
s=""
r=0
for i in range(0,len(num)):
    for j in range(i,len(num)):
        s=s+num[j]
        if(s[::-1]==s):
            r=len(num)-len(s)
            lis.append(r)
    s=""
print(min(lis))
