while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
        continue

    digit = 0
    d = {0:0, 1: 1}

    loop = True
    while loop:
        digit += 1
        square = 10 ** digit
        add = square % n

        pairs = list(d.items())
        for key, value in pairs:
            next_key = key + square
            next_value = (value + add) % n
            if next_value == 0:
                loop = False
                print(next_key)
                break
            d[next_key] = next_value
