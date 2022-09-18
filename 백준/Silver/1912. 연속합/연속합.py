n = int(input())
nums = list(map(int, input().split()))

sums = [nums[0]]
for num in nums[1:]:
    sums.append(sums[-1] + num)

min_, max_ = 0, sums[0]
for sum_ in sums:
    current = sum_ - min_
    min_ = min(sum_, min_)
    max_ = max(current, max_)
print(max_)
