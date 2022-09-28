from collections import defaultdict

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
hash_x, hash_y = defaultdict(int), defaultdict(int)
for x, y in points:
    hash_x[x] += 1
    hash_y[y] += 1

count = 0
for hash in [hash_x, hash_y]:
    for key, value in hash.items():
        if value > 1:
            count += 1
    
print(count)