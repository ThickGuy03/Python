import math
def obwod(a,b,c):
    O=a+b+c
    return O
def pole(a,b,c):
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
def czy_rownoboczny(a,b,c):
    if a==b==c:
        return print("Trójkąt jest równoboczny")
    elif a==b or b==c or a==c:
        return print("Trójkąt jest równoramienny")
    else:
        return print("Trójkąt jest różnoboczny")
def czy_prostokatny(tab):
    if tab[0]**2+tab[1]**2==tab[2]**2:
        return print("Trójkąt jest prostokątny")
    elif tab[0]**2+tab[1]**2>=tab[2]**2 and tab[1]**2+tab[2]**2>=tab[0]**2 and tab[2]**2+tab[0]**2>=tab[1]**2:
        return print("Trójkąt jest ostrokątny")
    elif tab[0]**2+tab[1]**2<=tab[2]**2:
        return print("Trójkąt jest rozwartokątny")
