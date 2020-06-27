list1 = [1,2,"s"]
list1.append(5);

# or
list1 = list1 + [55,"er"]
print(list1);
print(list1[3]);
del list1[3];
print(list1);
print(list1.index("er"))

#list1.sort()
print(list1)

l1=["c",'a','f','b','d','e']
l2='ghijklmnopqrstuvwxyz'
l1.sort()
print(l1)
print(l2)

l3='*'.join(l1)
print(l3)
l1=''.join(l1)
print(l1)
l3=l1+l2
print(l3)