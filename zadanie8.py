a=int(input())
b=int(input())
c=0
z=0
if a>b:
    c=a
    a=b
    b=c 
    print("zamieniono wartości zmiennych")
z=b%a
z*=z+3
print(z)



    