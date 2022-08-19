import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        p = int(input())
        max_price = -1
        max_name = ""
        for _ in range(p):
            price, name = input().split()
            price = int(price)
            if price > max_price:
                max_price = price
                max_name = name
        print(max_name)

