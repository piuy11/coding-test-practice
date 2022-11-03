import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

word_count = defaultdict(int)
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        word_count[word] += 1
words = list(word_count.keys())
words.sort(key=lambda word: (-word_count[word], -len(word), word))
print("\n".join(words))
