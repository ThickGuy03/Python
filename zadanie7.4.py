def Pascal(n):
    tab=[]
    while(n>0):
        for i in range(1,len(tab)):
            tab[i]=tab[i]+tab[i-1]
        tab.append(1)
        przerwa=""
        for i in range(0,int(n/2)):
            przerwa+="\t"
        for i in enumerate(tab):
            if (n % 2 == 1):
                przerwa += "   "
            przerwa += str(i[1]) + "\t"
        print(przerwa)
        n=n-1
n=int(input("Podaj ile chcesz mieć rzędów trójkąta pascala: "))
print(Pascal(n))