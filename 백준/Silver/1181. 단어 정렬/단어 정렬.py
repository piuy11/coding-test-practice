import sys
input = sys.stdin.readline

n = int(input())
words = list(set([input().strip() for _ in range(n)]))
words.sort(key=lambda word: (len(word), word))
print("\n".join(words))