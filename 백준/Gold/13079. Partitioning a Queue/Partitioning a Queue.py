import sys

input = sys.stdin.readline


def run(n, m, k):
    if dp[n] != -1:
        return dp[n]

    dp[n] = 0
    if not (n >= m and (n - m) % k == 0):
        dp[n] += 1
    
    for i in range(1, n):
        if not (i >= m and (i - m) % k == 0):
            dp[n] += run(n-i, m, k)
    return dp[n]
        



if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, m, k = list(map(int, input().split()))
        dp = [-1 for _ in range(n + 1)]
        print(run(n, m, k))
        # print(dp)
