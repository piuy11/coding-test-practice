import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())
seq = sorted(list(map(int, input().split())))

for pick in combinations_with_replacement(seq, m):
    print(" ".join([str(i) for i in pick]))
