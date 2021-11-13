def fib(N):
    if N in {0, 1}:
        return N
    return fib(N - 1) + fib(N - 2)

N = int(input("Podaj ilosc wyrazow ciagu Fibonacci: "))

for A in range(0,N):
    print(fib(A))