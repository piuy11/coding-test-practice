from collections import defaultdict


def flip(num):
    return int(str(num)[::-1])


T = int(input())
for loop in range(T):
    n = int(input())

    cache = defaultdict(bool)
    nexts = []
    currents = [0]
    count = 0
    do_break = False
    while True:
        count += 1
        for current in currents:
            if current in cache:
                continue
            cache[current] = True

            next1 = current + 1
            next2 = flip(current)
            if n in (next1, next2):
                do_break = True
                break

            # 1. 이미 cache에 존재
            # 2. nexts에 존재
            # 3. currents에 존재

            if not (next1 in cache or next1 in nexts or next1 in currents or next1 > n):
                nexts.append(next1)

            if not (next2 in cache or next2 in nexts or next2 in currents or next2 > n):
                nexts.append(next2)
        if do_break:
            break

        currents = nexts
        nexts = []
    print(f"Case #{loop+1}: {count}")
