s = input()

found_bracket = False
index = 0
result = ""
for i, c in enumerate(s):
    if not found_bracket and c == "<":
        found_bracket = True
        result += " ".join(word[::-1] for word in s[index:i].split())
        index = i
    elif found_bracket and c == ">":
        found_bracket = False
        result += s[index:i+1]
        index = i + 1
result += " ".join(word[::-1] for word in s[index:].split())
print(result)