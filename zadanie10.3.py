lista=[]
for i in range(100,401):
    a=(i%1000)//100
    b=(i%100)//10
    c=i%10
    if a%2==0 and b%2==0 and c%2==0:
        lista.append(i)
print(lista)