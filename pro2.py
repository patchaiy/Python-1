from itertools import combinations
Num,dig=map(int,input().split())
l=len(str(Num))
lst1=list(combinations(str(Num),l-dig))
lst1=sorted(lst1)
print(*lst1[0],sep='')
