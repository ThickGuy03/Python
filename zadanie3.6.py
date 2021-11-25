def generuj(n):
    for i in range(1,n+1):
         print("a["+str(i-1)+"]="+"look-and-say"*i)
n=int(input("Podaj liczbe wyrazów ciągów które chcesz zobaczyć: "))
generuj(n)