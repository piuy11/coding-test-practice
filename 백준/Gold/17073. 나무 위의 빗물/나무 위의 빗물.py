import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, w = map(int, input().split())
adjacent_list = defaultdict(list)
checked = defaultdict(bool)
for _ in range(n-1):
    u, v = map(int, input().split())
    adjacent_list[u].append(v)
    adjacent_list[v].append(u)

# find leaf nodes of tree
queue = deque([1])
leaves_count = 0
if n == 1 or n == 2:
    print(w)
else:
    while len(queue) > 0:
        node = queue.pop()
        checked[node] = True

        if len(adjacent_list[node]) == 1 and node != 1:
            leaves_count += 1

        for i in adjacent_list[node]:
            if not checked[i]:
                queue.append(i)

    print(w / leaves_count)