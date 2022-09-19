n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
min_ = [0, 0, 0]

for r, g, b in rgb:
    min_ = [
        r + min(min_[1], min_[2]), 
        g + min(min_[0], min_[2]),
        b + min(min_[0], min_[1]),
    ]
print(min(min_))