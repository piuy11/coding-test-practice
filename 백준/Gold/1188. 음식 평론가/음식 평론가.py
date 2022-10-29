import math

n, m = map(int, input().split())
if n % m == 0:
    print(0)
else:
    gcd = math.gcd(n, m)
    print(m - gcd)
    