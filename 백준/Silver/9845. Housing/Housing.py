# 9845

n = int(input())
dp = [[-1 for _ in range(20)] for _ in range(101)]

def run(m, length):
    if dp[m][length] != -1:
        return dp[m][length]
    
    if length == 1:
        result = 1
    elif length == 2:
        result = int((m+2)/2)
    else:
        result = 0
        for i in range(m, -1, -length):
            result += run(i, length - 1)

    dp[m][length] = result
    return result

sum_ = 0
for i, j in enumerate(range(n, 4, -5), start=1):
    sum_ += run(j-5, i)

print(sum_)
