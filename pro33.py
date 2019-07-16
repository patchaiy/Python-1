s=input()
lis=[]
for i in range(1,len(s)):
    o=ord(s[i])
    lis.append(o)
m=max(lis)
m=chr(m)
letter=s.find(m)
ans=s[letter:]
print(ans)
