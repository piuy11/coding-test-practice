import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
bfs = deque([s])
cost = {s: 0}
if s == g:
    print(0)
else:
    while len(bfs) != 0:
        current = bfs.popleft()
        up = current + u
        down = current - d        

        if up <= f and up not in cost:
            bfs.append(up)
            cost[up] = cost[current] + 1
        if down >= 1 and down not in cost:
            bfs.append(down)
            cost[down] = cost[current] + 1

        if up == g or down == g:
            break

    if g not in cost:
        print("use the stairs")
    else:
        print(cost[g])