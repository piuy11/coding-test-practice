import sys
from itertools import compress, product

input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
table = [list(map(int, input().split())) for _ in range(n)]

min_price = 10000
min_nums = []
for selector in product([0, 1], repeat=n):
    if all(i == 0 for i in selector):
        continue
    select = list(compress(table, selector))
    sums = [sum(row) for row in zip(*select)]
    if any([i < j for i, j in zip(sums[:-1], target)]):
        continue
    if sums[-1] < min_price:
        min_price = sums[-1]
        min_nums = list(compress(range(1, n+1), selector))
    elif sums[-1] == min_price:
        index = list(compress(range(1, n+1), selector))
        if index < min_nums:
            min_price = sums[-1]
            min_nums = index

if len(min_nums) == 0:
    print(-1)
else:
    print(min_price)
    print(" ".join([str(i) for i in min_nums]))

