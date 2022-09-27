n = int(input())
print("\n".join(map(str, sorted([int(input().strip()) for _ in range(n)]))))