import sys


def max_with_none(a, b):
    if a is None:
        if b is None:
            return None
        else:
            return b
    else:
        if b is None:
            return a
        else:
            return max(a, b)


input = sys.stdin.readline
s = input().strip()
# last is num1, num2, calculator case
if s[0] == "+":
    num1 = 10
else:
    num1 = 1
max_values = [num1, None, None]

for i, c in enumerate(s[1:], start=1):
    # num1
    if max_values[2] is None:
        num1 = None
    else:
        if c == "+":
            if s[i - 1] == "+":
                num1 = max_values[2] + 10
            else:
                num1 = max_values[2] - 10
        else:
            if s[i - 1] == "+":
                num1 = max_values[2] + 1
            else:
                num1 = max_values[2] - 1

    # num2
    if s[i - 1] == "+" and c == "-":
        if max_values[0] is None:
            num2 = None
        else:
            if i == 1 or s[i - 2] == "+":
                num2 = max_values[0] + 1  # +10 -> +11
            else:
                num2 = max_values[0] - 1  # -10 -> -11
    else:
        num2 = None

    # cal
    cal = max_with_none(max_values[0], max_values[1])
    max_values = [num1, num2, cal]

print(max_with_none(max_values[0], max_values[1]))
