import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, m = list(map(int, input().split()))
points = sorted(list(map(int, input().split())))

for _ in range(m):
    x, y = list(map(int, input().split()))
    print(bisect_right(points, y) - bisect_left(points, x))