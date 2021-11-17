def harmoniczny(n):
    if n==1:
        return 1
    else:
        return 1/n
n=int(input("Podaj liczbe wyrazów ciągu harmonicznego: "))
tab=[]
x=1
while x<=n:
    tab.append(harmoniczny(x))
    x+=1
wynik=sum(tab)
print("Suma ",n," wyrazów ciagu harmonicznego wynosi ",wynik)