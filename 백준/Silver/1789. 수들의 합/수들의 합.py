n = int(input())
i = 1
sum_ = 0
while True:
    sum_ += i
    if sum_ > n:
        break
    i += 1
print(i - 1)
