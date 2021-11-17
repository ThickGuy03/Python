def bez_powtorzen(x):
    x.sort()
    x=list(dict.fromkeys(x))  
    return x

N=int(input("podaj liczbe elemntów tabicy: "))
print("Wpisz elemnty tablicy: ")
tab=[]
for i in range(0,N):
    element=int(input())
    tab.append(element)
print(tab)
print(bez_powtorzen(tab))


