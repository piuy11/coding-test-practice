import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())
adjacent_list = defaultdict(set)
for _ in range(m):
    x, y = list(map(int, input().split()))
    adjacent_list[x].add(y)
    adjacent_list[y].add(x)

infected = set([1])
check_list = set(adjacent_list[1])
while True:
    len_before = len(infected)
    infected.update(check_list)

    if len(infected) == len_before:
        break
    
    next_check_list = set()
    for i in check_list:
        next_check_list.update(adjacent_list[i])
    check_list = next_check_list
    

print(len(infected) - 1)

