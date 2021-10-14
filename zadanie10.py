import cmath 
from cmath import cos,sin
z=1j
a=z.imag
b=z.real
q=int((sin(z)**2+cos(z)**2).real)
print(q)
print(bool(q==1))