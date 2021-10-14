import cmath
from cmath import *
from math import *
print("Wprowadź liczbe zespoloną")
z=complex(input())
a=z.real/abs(z)
q=z.imag/abs(z)
print("moduł z liczby "+str(z) +" = "+ str(abs(z)))
print((cos(a)*2*pi)/360)
print(complex(abs(z)*(cos(a)+(sin(q)))))
print(z.conjugate())
