from collections import defaultdict
from itertools import chain

a, b = input().split()
n, m = list(map(int, input().split()))

converts = defaultdict(list)
for _ in range(m):
    from_, to_ = input().split()
    converts[from_].append(to_)
    converts[to_].append(from_)

count_ = 0
bfs = set(a)
is_checked = defaultdict(bool)
found = False
while True:
    if b in bfs:
        break

    next_bfs = set()
    for from_ in bfs:
        if not is_checked[from_]:
            is_checked[from_] = True
            next_bfs.update(converts[from_])

    if len(next_bfs) == 0:
        count_ = -1
        break

    bfs = next_bfs
    count_ += 1


print(count_)