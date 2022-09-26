strokes = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
alphabets = list(map(chr, range(ord("A"), ord("Z") + 1)))
strokes_dict = {a: s for a, s, in zip(alphabets, strokes)}

n, m = list(map(int, input().split()))
s1, s2 = list(map(list, input().split()))

cal = []
for i, (c1, c2) in enumerate(zip(s1, s2)):
    cal.append(strokes_dict[c1])
    cal.append(strokes_dict[c2])
if len(s1) > len(s2):
    cal.extend([strokes_dict[c] for c in s1[i+1:]])
elif len(s1) < len(s2):
    cal.extend([strokes_dict[c] for c in s2[i+1:]])

while len(cal) > 2:
    new_cal = []
    for i, j in enumerate(cal[1:], start=1):
        new_cal.append(cal[i-1] + j)
    cal = new_cal
c = str(cal[0])[-1]
if c == "0":
    c = ""
print(c + str(cal[1])[-1] + "%")
