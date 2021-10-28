a=int(input("Wprowadź liczbe całkowitą: "))
reszta=a%2
if reszta==0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

#bez uzycia funkcji if 
lista=[reszta]
print (0 in lista)