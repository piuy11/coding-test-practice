import re

n = int(input())
for _ in range(n):
    s = input().strip()
    if re.match(r"^[ABCDEF]?A+F+C+[ABCDEF]?$", s):
        print("Infected!")
    else:
        print("Good")
