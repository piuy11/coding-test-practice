import sys

input = sys.stdin.readline


def check_near(p1, p2):
    # print(p1, p2)
    same_count, diff_count = 0, 0
    for i, j in zip(p1, p2):
        if i == j:
            same_count += 1
        elif i - j == 1 or j - i == 1:
            diff_count += 1
    if same_count == 2 and diff_count == 1:
        # print(True)
        return True
    else:
        # print(False)
        return False


def run(points):
    if points[0] != (0, 0, 0):
        return "NO 1"
    near_count = 0
    for i, p1 in enumerate(points[1:], start=1):
        current_near_count = 0
        # 이전 점들 중 인접하는지 확인
        for p2 in points[:i]:
            if check_near(p1, p2):
                current_near_count += 1
            elif p1 == p2:
                return f"NO {i+1}"
        if current_near_count == 0:
            return f"NO {i+1}"
        near_count += current_near_count
    # print(near_count)
    return 6 * len(points) - 2 * near_count


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        p = int(input())
        points = []
        for _ in range((p + 7) // 8):
            points.extend(
                [tuple(map(int, point.split(","))) for point in input().strip().split()]
            )
        print(run(points))

