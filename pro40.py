st1="dhoni"
st2=input()
val1=list(set(st1)-set(st2))
val2=list(set(st2)-set(st1))
val=len(val1)+len(val2)
if val==0:
	print("yes")
else:
	print("no")
