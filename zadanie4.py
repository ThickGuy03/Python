a=input()
for i in range(0,len(a)):
    if a[0]==a[i+1]:
        a[i+1]='$'
print(a)
        