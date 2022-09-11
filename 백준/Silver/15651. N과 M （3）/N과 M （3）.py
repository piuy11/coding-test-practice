from itertools import product

n, m = list(map(int, input().split()))
for seq in product(range(1, n + 1), repeat=m):
    print(" ".join(str(i) for i in seq))
