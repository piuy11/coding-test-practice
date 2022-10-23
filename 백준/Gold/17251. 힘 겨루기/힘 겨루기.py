import sys

input = sys.stdin.readline

n = int(input())
lines = list(map(int, input().split()))

max_ = 0
max_indices = []
for i, j in enumerate(lines):
    if j > max_:
        max_ = j
        max_indices = [i]
    elif j == max_:
        max_indices.append(i)
    
a = max_indices[0]
b = n - max_indices[-1] - 1

if a < b:
    print("R")
elif a > b:
    print("B")
else:
    print("X")