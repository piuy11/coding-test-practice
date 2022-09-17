T = int(input())
lengths = [int(input()) for _ in range(T)]
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, max(lengths)+1):
    dp.append(dp[i-1] + dp[i-5])
for length in lengths:
    print(dp[length])