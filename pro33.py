s=input()
for i in range(1,len(s)):
    if ord(s[i])>ord(s[0]):
        ans=s[i:]
print(ans)
