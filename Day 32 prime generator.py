
import sympy

t = int(input())
for _ in range(t):
    N1, N2 = map(int, input().split())
    for Num in range(N1, N2 + 1):
        if sympy.isprime(Num):
            print(Num)
    else:
        print()
