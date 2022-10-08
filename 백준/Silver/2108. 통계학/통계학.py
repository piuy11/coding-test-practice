from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

# 산술평균
print(round(sum(nums) / len(nums)))

# 중앙값
print(nums[int((len(nums) - 1) / 2)])

# 최빈값
count = Counter(nums)
max_count = max(count.values())
max_keys = sorted([key for key, value in count.items() if value == max_count])
print(max_keys[1] if len(max_keys) > 1 else max_keys[0])

# 범위
print(nums[-1] - nums[0])