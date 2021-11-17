import math
def konwertuj(N,R):
    if  R=="r":
        wynik=N*math.pi/180
    elif R=="s":
        wynik=N*180/math.pi
    else:
        print("Wybrano nie istniejącą metodę konwersji")
    return wynik
print("Na Radiany -> r || Na Stopnie -> s")
N=float(input("Podaj liczbe stopni lub radianów: "))
R=input("Podaj metode zamiany: ")
print("Wynik konwerji to: ",konwertuj(N,R))

