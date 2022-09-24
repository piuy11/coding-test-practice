def run(x, y):

    root = (x+y) ** 0.5
    if root != int(root) or x == 2 or y == 2:
        return -1
    
    if x == 0:
        return 0

    # check odd, even
    dividee = x % 2

    sum_ = 0
    for i, n in enumerate(range(2 * int(root) -1, -1, -2), start=1):
        sum_ += n
        if sum_ >= x and i % 2 == dividee:
            break
    return i

x, y = list(map(int, input().split()))
print(run(x, y))