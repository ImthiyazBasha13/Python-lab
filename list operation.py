list1 = [1,2,3,4,5]
list1.append(6)
list1.insert(3,10)
list1.pop()
list1.sort()
print(max(list1))
print(min(list1))
print(sum(list1))

list2=[10,11,12,13,14,15]
res = list1+list2
print(res)
l1=set(list1)
l2=set(list2)
if(l1&l2):
    print(l1 &l2)
else:
    print("No comomon elements")

n=int(input("Enter the element u want to  search:"))
for i in list1:
    if(n!=i):
        pass
    else:
        print("TRUE")
print(list1)
        
        

