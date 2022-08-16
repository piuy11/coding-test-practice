import string


def run(s: str, n: int):
    if n == 1:
        return "1 1"

    indices = {c: [] for c in string.ascii_lowercase}
    min_, max_ = len(s), 0
    for i, c in enumerate(s):
        indices[c].append(i)
        if len(indices[c]) == n:
            length = indices[c][-1] - indices[c][0] + 1
            if length < min_:
                min_ = length
            if length > max_:
                max_ = length
            del indices[c][0]

    if min_ == len(s) and max_ == 0:
        return "-1"
    else:
        return f"{min_} {max_}"


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = input()
        n = int(input())
        print(run(s, n))

