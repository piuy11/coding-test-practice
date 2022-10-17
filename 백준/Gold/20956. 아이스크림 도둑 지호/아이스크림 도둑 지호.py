import sys
from bisect import insort
from collections import defaultdict

input = sys.stdin.readline

n, m = list(map(int, input().split()))
weights = list(map(int, input().split()))

weight_dict = defaultdict(list)
for i, weight in enumerate(weights, start=1):
    insort(weight_dict[weight], i)

reverse = False
answer = []
for key, value in sorted(weight_dict.items(), reverse=True):
    if key % 7 != 0:
        if reverse:
            answer.extend(value[::-1])
        else:
            answer.extend(value)
    else:
        default_range = iter(range(len(value)))
        reverse_range = iter(range(len(value) - 1, -1, -1))
        for _ in value:
            if reverse:
                answer.append(value[next(reverse_range)])
            else:
                answer.append(value[next(default_range)])
            reverse = not reverse      

print("\n".join([str(i) for i in answer[:m]]))
