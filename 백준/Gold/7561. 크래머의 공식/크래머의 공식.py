import sys
from copy import deepcopy

input = sys.stdin.readline

def det(a):
    return a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])- a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0]) + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0])

def change_column(a, b, index):
    result = deepcopy(a)
    for i, _ in enumerate(result):
        result[i][index] = b[i]
    return result



T = int(input())
for case_num in range(T):
    lines = [list(map(int, input().split())) for _ in range(3)]
    A = [line[:3] for line in lines]
    B = [line[3] for line in lines]
    # det_Ai = (det([B, A[1], A[2]]), det([A[0], B, A[2]]), det([A[0], A[1], B]))
    det_Ai = (det(change_column(A, B, 0)), det(change_column(A, B, 1)), det(change_column(A, B, 2)))
    det_A = det(A)

    print(" ".join([str(i) for i in det_Ai] + [str(det_A)]))
    if det_A == 0:
        print("No unique solution")
    else:
        xs = [i / det_A for i in det_Ai]
        xs = [i if i <= -0.0005 or i >= 0.0005 else 0 for i in xs]
        xs = [format(i, '.03f') for i in xs]
        print(f"Unique solution: {' '.join(xs)}")
    
    if case_num != T - 1:
        print("\n", end="")
