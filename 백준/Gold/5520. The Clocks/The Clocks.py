moves_alpha = ["ABDE", "ABC", "BCEF", "ADG", "BDEFH", "CFI", "DEGH", "GHI", "EFHI"]
# moves = [(ord(c) - ord("A") for c in s) for s in moves_alpha]
moves = [
    tuple(1 if chr(ord("A") + i) in s else 0 for i in range(9)) for s in moves_alpha
]

target_clocks = []
for _ in range(3):
    target_clocks.extend(list(map(int, input().split())))

clock = [0 for _ in range(9)]
count = [0 for _ in range(9)]
found = False


def back_track(depth):
    global clock, found
    if depth == 9:
        # print(clock)
        # print(count)
        # input()
        if clock == target_clocks:
            found = True
        return
    for i in range(4):
        count[depth] = i
        back_track(depth + 1)
        if found:
            break
        clock = [(i - j) % 4 for i, j in zip(clock, moves[depth])]


back_track(0)
result = []
for i, rotate in enumerate(count):
    if rotate > 0:
        result.extend([str(i + 1) for _ in range(rotate)])

print(" ".join(result))
