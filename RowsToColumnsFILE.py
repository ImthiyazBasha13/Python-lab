file = open("filetest.txt")
columnlist=[]
for name in file:
    columnlist.append(name)
print(columnlist)