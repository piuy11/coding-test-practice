def check_diff(word1, word2):
    if len(word1) + 1 != len(word2):
        return False

    i1, i2 = 0, 0
    count = 0
    while i1 < len(word1) and i2 < len(word2):
        # print(i1, i2, word1[i1], word2[i2])
        if word1[i1] == word2[i2]:
            i1 += 1
        else:
            count += 1
            if count > 1:
                return False
        i2 += 1
    return True


if __name__ == "__main__":
    n, origin_word = input().split()
    n = int(n)

    words = [origin_word]
    for _ in range(n):
        words.append(input())
    words = list(set(words))
    words.sort(key=lambda x: len(x))

    # 다음 length로 연결되어있는 단어의 index
    next_index = [[] for _ in words]
    len_before = -1
    start, end = 0, 0
    for i, word in enumerate(words):
        if len_before != len(word):
            len_before = len(word)
            start = end
            end = i
            # print(start, end)

        # checklist
        for j in range(start, end):
            # diff is 1
            if check_diff(words[j], word):
                next_index[j].append(word)

    # bfs
    bfs = [origin_word]
    last_word = origin_word
    for i, (word, next) in enumerate(zip(words, next_index)):
        if word in bfs and len(next) > 0:
            last_word = next[0]
            bfs.extend(next)

    print(last_word)
