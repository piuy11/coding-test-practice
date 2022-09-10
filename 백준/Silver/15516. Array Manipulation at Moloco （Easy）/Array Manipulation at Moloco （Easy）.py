def binary_search(arr, n):
    index = len(arr) // 2
    if len(arr) == 1:
        if arr[index] >= n:
            return 0
        else:
            return 1
    if arr[index] >= n:
        return binary_search(arr[:index], n)
    else:
        return index + binary_search(arr[index:], n)


def run(arr):
    sorted_list = [arr[0]]
    result = [0]
    for i in arr[1:]:
        index = binary_search(sorted_list, i)
        sorted_list.insert(index, i)
        result.append(index)
    return result


if __name__ == "__main__":
    length = int(input())
    arr = []
    for _ in range(length):
        arr.append(int(input()))

    result = run(arr)
    for i in result:
        print(i)
