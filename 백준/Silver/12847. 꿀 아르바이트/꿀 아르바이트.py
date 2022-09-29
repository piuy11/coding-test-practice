n, m = list(map(int, input().split()))
pay = list(map(int, input().split()))

sum_ = sum(pay[:m])
max_ = sum_
for i in range(m, n):
    sum_ += pay[i]
    sum_ -= pay[i-m]
    if sum_ > max_:
        max_ = sum_
print(max_)
