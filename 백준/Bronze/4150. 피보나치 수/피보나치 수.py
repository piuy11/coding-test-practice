n = int(input())
fib = [-1 for _ in range(n+2)]
fib[1] = 1
fib[2] = 1

for i in range(3, n+1):
    fib[i] = fib[i-2] + fib[i-1]

print(fib[n])
