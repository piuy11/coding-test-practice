import math


def run(R, n):
    theta = math.pi * (n - 2) / n
    cos_theta_2 = math.cos(theta / 2)
    return cos_theta_2 * R / (cos_theta_2 + 1)


T = int(input())
for i in range(T):
    R, n = input().split()
    R, n = float(R), int(n)
    print(f"Scenario #{i+1}:")
    print(format(run(R, n), ".3f"))
    print()
