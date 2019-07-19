s=input()
s=s.lower()
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=s.replace(" ","")
lis=list(s)
lis.sort()
if l==lis:
  print("yes")
else:
  print("no")
