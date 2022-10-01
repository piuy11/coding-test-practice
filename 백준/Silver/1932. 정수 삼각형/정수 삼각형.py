n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
max_ = [tri[0][0]]

for layer in tri[1:]:
    max_ = [layer[0] + max_[0]] + [k + max(i, j) for i, j, k in zip(max_[:-1], max_[1:], layer[1:-1])] + [layer[-1] + max_[-1]]

print(max(max_))
