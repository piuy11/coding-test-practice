from bisect import bisect_left

n = int(input())
lengths = [int(input()) for _ in range(n)]
q = int(input())
targets = [int(input()) for _ in range(q)]

indices, values = [], []
for length in lengths:
    count = 1
    while length % 2 == 0:
        count += 1
        length = int(length / 2)

    index = 2 ** (count - 1)
    if not indices:
        indices.append(index)
    else:
        indices.append(indices[-1] + index)
    values.append(length)
# print(indices, values)

for target in targets:
    index = bisect_left(indices, target)
    print(values[index])

