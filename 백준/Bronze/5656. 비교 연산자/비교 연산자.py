i = 1
while True:
    s = input()
    if "E" in s:
        break
    print(f"Case {i}: {'true' if eval(s) else 'false'}")
    i += 1