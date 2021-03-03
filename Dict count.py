from collections import *
d= defaultdict(int)
s= str(input("Enter String"))
for w in s.split():
    d[w]+=1
print(d)