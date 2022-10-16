import sys

lines = sys.stdin.readlines()

for line in lines:
    n = int(line)
    m = 1
    digit = 1
    while True:
        if m % n == 0:
            break
        m = m * 10 + 1
        digit += 1

    print(digit)