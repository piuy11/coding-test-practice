import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x, y = list(map(int, input().split()))

print(int(n * x / 100), len([1 for i in arr if i >= y]))
