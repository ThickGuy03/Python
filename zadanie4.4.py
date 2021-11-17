def n_element_ciagu(n):
    a=1
    q=2
    if n==1:
        return a
    for i in range(1,n):
        a*=q
    return a
n=int(input("Dla którego wyrazu ciągu geometrycznego chcesz zobaczyć wartość? "))
print("Wartość "+str(n)+"-ego wyrazu ciągu wynosi: ")
print(n_element_ciagu(n))