def suma_elementow(x):
    suma=0
    dlugosc=len(x)
    for i in range(0,dlugosc):
        suma=suma+x[i]
    return suma

N=int(input("Podaj liczbe elementów listy"))
print("Wpisz elementy listy")
tab=[]
for i in range(0,N):
    element=int(input())
    tab.append(element)
print("Suma elementów tablicy wynosi: ",suma_elementow(tab))