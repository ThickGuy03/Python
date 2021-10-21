newList=[]
a=0
for i in range(3,100,3):
    newList.extend([i])
print(newList)
for c in newList:
    a+=1
    print(a)
    if a==3:
        newList.remove(c)
        a=1
print(newList)
total=0
for i in newList:
    total=total+i
x=total/len(newList)
print(x)