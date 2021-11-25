import trojkat

print("Podaj długości trzech boków trójkąta: ")
a=int(input())
b=int(input())
c=int(input())
tab=[a,b,c,]
tab.sort()
if tab[0]+tab[1]>tab[2]:
    print("istnieje taki trójkąt")
    print("Obwód trójkąta wynosi: ",trojkat.obwod(a,b,c))
    print("Pole trójkąta wynosi: ",trojkat.pole(a,b,c))
    trojkat.czy_rownoboczny(a,b,c,)
    trojkat.czy_prostokatny(tab)