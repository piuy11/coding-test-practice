n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
happy_frugal = [(j/p, p, i) for i, (j, p) in enumerate(matrix)]
happy_frugal.sort(reverse=True)

print(sum([i for _, i, _ in happy_frugal[:3]]))
for _, _, i in happy_frugal[:3]:
    print(i+1)


