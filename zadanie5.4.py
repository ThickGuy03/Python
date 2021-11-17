import itertools
lista=[]
print("Podaj liczbe elementów w liście: ")
n=int(input())
print("Wpisuje kolejne wartości listy")
for i in range(0,n):
    x=int(input())
    lista.append(x)
print(list(itertools.permutations(lista)))

