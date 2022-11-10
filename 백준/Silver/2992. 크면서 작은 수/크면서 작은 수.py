from bisect import bisect
from itertools import permutations

n = int(input())

chars = [i for i in str(n)]
s = set(permutations(chars, len(chars)))
s = sorted(list(s))
index = bisect(s, tuple(chars))
if index == len(s):
    print(0)
else:
    print("".join(s[index]))
