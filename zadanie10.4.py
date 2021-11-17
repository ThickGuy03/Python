def NWD(a,b):
    if b>a:
        temp=a
        a=b
        b=temp
        while a>b and b>0:
            c=a%b
            a=b
            b=c
    else:
         while a>b and b>0:
            c=a%b
            a=b
            b=c
    return a


print("Podaj dwie liczby całkowite")
a=int(input("A: "))
b=int(input("B: "))
print("Największy wspólny dzielnik tych liczb wynosi: ",NWD(a,b))