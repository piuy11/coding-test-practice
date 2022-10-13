def get_collatz(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        result.append(n)
    return result

while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    a_collatz = get_collatz(a)
    b_collatz = get_collatz(b)

    found = False
    for (i, a_k), (j, b_k) in zip(list(enumerate(a_collatz))[::-1], list(enumerate(b_collatz))[::-1]):
        if a_k != b_k:
            found = True
            break

    if found:
        i += 1
        j += 1
        a_k = a_collatz[i]

    print(f"{a} needs {i} steps, {b} needs {j} steps, they meet at {a_k}")