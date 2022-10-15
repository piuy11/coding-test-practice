import sys

input = sys.stdin.readline

m = int(input())
sum_, xor = 0, 0
for _ in range(m):
    query = input().split()
    if query[0] == "1":
        n = int(query[1])
        sum_ += n
        xor ^= n
    elif query[0] == "2":
        n = int(query[1])
        sum_ -= n
        xor ^= n
    elif query[0] == "3":
        print(sum_)
    elif query[0] == "4":
        print(xor)