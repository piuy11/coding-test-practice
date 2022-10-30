def calculate(num):
    if dp[num] != 0:
        return dp[num]
    else:
        result = calculate(num-1) + 2 * calculate(num-2)
        dp[num] = result
        return result

n = int(input())
dp = [0 for _ in range(max(3, n+1))]
dp[1] = 1
dp[2] = 3
calculate(n)
if n == 1 or n == 2:
    result = dp[n]
elif n % 2 == 0:
    result = (dp[n] + dp[n // 2] + 2 * dp[n // 2 - 1]) // 2
else:
    result = (dp[n] + dp[n // 2]) // 2
print(result)
