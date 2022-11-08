import sys
from bisect import bisect

input = sys.stdin.readline

n, s = map(int, input().split())
sizes = sorted([int(input()) for _ in range(n)])

sum_ = 0
for i, size in enumerate(sizes[1:], start=1):
    index = min(bisect(sizes, s - size), i)
    sum_ += index
print(sum_)
