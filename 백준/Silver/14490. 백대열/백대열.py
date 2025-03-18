from math import gcd

m, n = map(int,input().split(':'))
x = gcd(m, n)
print(f'{m // x}:{n // x}')