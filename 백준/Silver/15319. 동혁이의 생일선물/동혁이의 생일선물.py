import math


def run(x, k):
    if k == 1:
        return 1
    exp = int(math.log2(k))
    base = x ** exp
    k -= 2 ** exp
    bases = [x ** i for i in range(exp-1, -1, -1)]
    binary = [i == "1" for i in bin(k)[2:]]
    binary = [False for _ in range(len(bases)-len(binary))] + binary
    return base + sum([n for n, i in zip(bases, binary) if i])

n = int(input())
results = []
for _ in range(n):
    x, k = list(map(int, input().split()))
    results.append(run(x, k))
print(sum(results) % 1000000007)
