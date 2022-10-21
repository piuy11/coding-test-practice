import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())
ladder = dict()
for _ in range(n + m):
    _from, _to = map(int, input().split())
    ladder[_from] = _to

visited = defaultdict(bool)
queue = deque([1])
next_queue = deque()
rolled = 1
while True:
    current = queue.pop()
    for i in range(1, 7):
        _next = current + i
        if _next in ladder:
            _next = ladder[_next]
        # check answer
        if _next == 100:
            break
        if not visited[_next]:
            visited[_next] = True
            next_queue.append(_next)
    
    if _next == 100:
        break
    
    if len(queue) == 0:
        queue = next_queue
        next_queue = deque()
        rolled += 1

print(rolled)

