n = int(input())
dice = list(map(int, input().split()))
if n == 1:
    print(sum(sorted(dice)[:5]))
else:
    availables = {
        3: [(0, 1, 2), (0, 2, 4), (0, 3, 4), (0, 1, 3), (5, 1, 2), (5, 2, 4), (5, 3, 4), (5, 1, 3)],
        2: [(0, 1), (0, 2), (0, 3), (0, 4), (5, 1), (5, 2), (5, 3), (5, 4), (1, 2), (2, 4), (3, 4), (1, 3)]
    }
    values = {n: min([sum([dice[i] for i in candidate]) for candidate in candidates]) for n, candidates in availables.items()}
    values[1] = min(dice)
    print(values[3] * 4 + values[2] * (4 * (2*n - 3)) + values[1] * (5 * (n-2) ** 2 + 4 * (n-2)))

