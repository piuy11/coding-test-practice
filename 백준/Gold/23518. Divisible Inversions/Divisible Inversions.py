n = int(input())
perm = list(map(int, input().split()))

n_divider = [0 for _ in range(n + 1)]

# i의 배수에 약수 개수 추가해서
# 약수 구하기
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        n_divider[j] += 1

count = 0
for index, i in enumerate(perm):
    count += n_divider[i]
    for j in range(i, n + 1, i):
        n_divider[j] -= 1

print(count)
