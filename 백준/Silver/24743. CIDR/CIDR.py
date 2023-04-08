n = int(input())

inputs = []
for _ in range(n):
    xs = [int(x) for x in input().split(".")]
    inputs.append(sum([x * (256 ** i) for i, x in enumerate(reversed(xs))]))

xors = [f'{inputs[0] ^ x:032b}' for x in inputs]
found = False
for i in range(32):
    if not all(x[i] == "0" for x in xors):
        found = True
        break

if n == 1 or i == 0 or not found:
    print(32)
else:
    print(i)
