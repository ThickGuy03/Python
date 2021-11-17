def silnia(n):
    silnia=1
    for i in range(1,n+1):
        silnia*=i
    return silnia

n=int(input("Podaj liczbe z której chcesz obliczyć silnie: "))
if n<=0:
    exit
else:
    print("silnia z liczby ",n," wynosi: ",silnia(n))