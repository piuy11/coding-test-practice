N, B = (int(i) for i in input().split())
Matrix = list[list[int]]
matrix: Matrix = []
for _ in range(N):
    matrix.append([int(i) % 1000 for i in input().split()])

# B를 2진법으로 변환
bases: list[int] = []
while B != 1:
    bases.append(B % 2)
    B //= 2
bases.append(1)

def mul_matrix(m1: Matrix, m2: Matrix) -> Matrix:
    m2_t = [[m2[i][j] for i in range(N)] for j in range(N)]
    mult = [
        [sum( [a*b for a, b in zip(m1[j], m2_t[i])] ) % 1000 for i in range(N)]
        for j in range(N)
    ]
    return mult


def double_matrix(m: Matrix) -> Matrix:
    m_t = [[m[i][j] for i in range(N)] for j in range(N)]
    mult = [
        [sum( [a*b for a, b in zip(m[j], m_t[i])] ) % 1000 for i in range(N)]
        for j in range(N)
    ]
    return mult
    

if bases[0] == 1:
    result = matrix
else:
    result = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

for base in bases[1:]:
    next_matrix = double_matrix(matrix)
    if base == 1:
        result = mul_matrix(result, next_matrix)
    matrix = next_matrix

for line in result:
    print(" ".join([str(i) for i in line]))
