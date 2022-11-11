from collections import deque

n = int(input())
queue = deque(range(1, n + 1))
answer = []
while len(queue) > 0:
    answer.append(queue.popleft())
    if len(queue) == 0:
        break
    queue.append(queue.popleft())
print(" ".join(map(str, answer)))