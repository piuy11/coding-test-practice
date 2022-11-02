T = int(input())
for _ in range(T):
    count = 0
    s = input()
    for c in s:
        if c == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count != 0:
        print("NO")
    else:
        print("YES")