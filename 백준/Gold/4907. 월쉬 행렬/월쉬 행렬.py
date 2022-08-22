import sys

input = sys.stdin.readline


def p(size, col, from_, to):
    if size == 1:
        return 1

    next_size = int(size / 2)

    if col >= next_size:
        down = True
    else:
        down = False

    # all row
    if to - from_ == size - 1:
        if down:
            return 0
        else:
            return 2 * p(next_size, col % next_size, from_, next_size - 1)

    if from_ >= next_size:
        if down:
            return -p(next_size, col % next_size, from_ % next_size, to % next_size)
        else:
            return p(next_size, col % next_size, from_ % next_size, to % next_size)
    elif to < next_size:
        return p(next_size, col % next_size, from_, to)
    else:
        if down:
            return p(next_size, col % next_size, from_ % next_size, next_size - 1) - p(
                next_size, col % next_size, 0, to % next_size
            )
        else:
            return p(next_size, col % next_size, from_ % next_size, next_size - 1) + p(
                next_size, col % next_size, 0, to % next_size
            )


def run(n, r, s, e):
    m = 2 ** n
    return p(m, r, s, e)


if __name__ == "__main__":
    while True:
        n, r, s, e = list(map(int, input().split()))
        if n == -1:
            break
        print(run(n, r, s, e))
