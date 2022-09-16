d, p = list(map(int, input().split()))
pipes = [] # (length, capacity)
for _ in range(p):
    l, c = list(map(int, input().split()))
    pipes.append((l, c))

# sort by (capacity, length)
pipes.sort(key=lambda x: (x[1], x[0]), reverse=True)

ables = [0]
for l, c in pipes:
    new_candidates = []
    for i in ables:
        candidate = i + l
        if candidate not in ables and candidate <= d:
            new_candidates.append(candidate)
    if d in new_candidates:
        break
    ables.extend(new_candidates)
print(c)