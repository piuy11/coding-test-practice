from collections import defaultdict, deque


def run(x, y):
    if x == y:
        return []
    elif x > y:
        return list(range(x, y, -1))
    bfs = deque()
    bfs.append([x])

    dp = defaultdict(bool)
    dp[x] = True

    # paths = []
    while True:
        paths = bfs.popleft()
        n = paths[-1]
        candidates = [n - 1, n + 1, n * 2]
        for candidate in candidates:
            if candidate == y:
                break
            if dp[candidate] or candidate < 0 or candidate > 100000:
                continue
            dp[candidate] = True
            bfs.append(paths + [candidate])

        if candidate == y:
            break
    
    return paths

x, y = list(map(int, input().split()))
paths = run(x, y)
print(len(paths))
# paths.append(y)
# print(" ".join([str(path) for path in paths]))

