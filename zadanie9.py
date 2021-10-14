import cmath
import math
print("Wprowadź liczbe zespoloną")
z=complex(input())
print(abs(z),cmath.phase(z))
a=z.real/abs(z)
q=z.imag/abs(z)
print(math.degrees(math.pi/6))
print("moduł z liczby "+str(z) +" = "+ str(abs(z)))
print(abs(z)*(math.cos(z)+math.sin(z)))
print(z.conjugate())
