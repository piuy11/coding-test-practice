import sys
from bisect import insort

input = sys.stdin.readline

registers = []
n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    insort(registers, end)
    insort(registers, start + 0.1)

count_ = 0
max_count = 0
for register in registers:
    if isinstance(register, float):
        count_ += 1
    else:
        count_ -= 1
    
    if count_ > max_count:
        max_count = count_

print(max_count)

