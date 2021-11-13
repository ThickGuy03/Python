M=int(input("Podaj liczbe kolumn: "))
N=int(input("Podaj liczbe wierszy: "))
tablica2D=[[0] * N for i in range(M)]
for i in range(M):
    for j in range(N):
        tablica2D[i][j]=i*j

print(tablica2D)