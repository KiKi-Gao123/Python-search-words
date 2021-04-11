#打印0,1,2,3,4,5,6,7,8,9

#常规方法
list1=[]
i=0
while i < 10:
    list1.append(i)
    i=i+1
print(list1)

#列表推导式
list2=[]
j=0
list2=[ j for j in range(10)]
print(list2)

#打印[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

#常规方法
list3=[]

for k in range(1,3):
    for m in range(3):
        list3.append((k,m))
print(list3)

#列表推导式
list3=[(k,m) for k in range(1,3) for m in range(0,3)]

print(list3)