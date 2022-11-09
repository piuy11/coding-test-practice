import sys
from itertools import count

input = sys.stdin.readline

availables = {
    1: {4, 5},
    2: {},
    3: {4, 5},
    4: {2, 3},
    5: {8},
    6: {2, 3},
    7: {8},
    8: {6, 7}
}

for nth in count(1):
    numbers = [int(c) for c in input().strip()]
    if numbers == [0]:
        break

    if numbers[0] != 1 or numbers[-1] != 2 or any([numbers[i+1] not in availables[numbers[i]] for i in range(len(numbers)-1)]):
        print(f"{nth}. NOT")
    else:
        print(f"{nth}. VALID")