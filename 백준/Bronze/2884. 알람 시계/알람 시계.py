h, m = list(map(int, input().split()))
time = (h * 60 + m - 45) % (24 * 60)
print(int(time / 60), time % 60)