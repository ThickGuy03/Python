from math import sqrt
a=int(input("Podaj wartość parametru a: "))
b=int(input("Podaj wartość parametru b: "))
c=int(input("Podaj wartość parametru c: "))
x1=0.0
x2=0.0
delta=(b^2)-(4*a*c)
print(delta)
if a==0:
    print("Podane równanie nie jest kwadratowe")
elif delta<0:
    print("brak rozwiązań")    
elif delta==0:
    x1=(-b)/2*a
    print(x1)
else :
    x1=(-b-sqrt(delta))/2*a
    x2=(-b+sqrt(delta))/2*a 
    print("x1= "+str(x1)+" x2= "+str(x2))