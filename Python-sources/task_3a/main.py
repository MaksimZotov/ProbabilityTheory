from decimal import Decimal
import math

P = 0.95
Q = 0.8

def fact(n):
    if n == 0: return Decimal(1)
    return Decimal(math.sqrt(2 * math.pi * n)) * ((Decimal(n) / Decimal(math.e)) ** Decimal(n))

def comb(m, n):
    return fact(n) / (fact(m) * fact(n - m))

n = 12200
sigma = 0
k_res = 0
for k in range(n + 1):
    m = n - k
    combination = comb(m, n)
    sigma += combination * (Decimal(P) ** Decimal(m)) * (Decimal(1 - P) ** Decimal(n - m))
    if sigma > 1 - Q:
        k_res = k
        break

