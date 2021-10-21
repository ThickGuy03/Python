import string
a=input()
klucz=a[0]
cenzura='$'
print(type(a))
print(type(klucz))
for i in range(0,len(a)):
    if klucz==a[i+1]:
        print(a[i+1])
        a=a[0:i] + cenzura + a[i+2:len(a-1)]
print(a)