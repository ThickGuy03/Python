import cmath 
from cmath import cos,sin
z=complex(input())
a=z.imag
b=z.real
print(bool(sin(b)**2+cos(a)**2==1))