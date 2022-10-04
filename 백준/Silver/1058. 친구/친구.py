n = int(input())
adj_list = [[i for i, c in enumerate(input().strip()) if c == "Y"] for _ in range(n)]

max_ = 0
for i, adj in enumerate(adj_list):
    friends = set(adj)
    for j in adj:
        friends.update(adj_list[j])
    if i in friends:
        friends.remove(i)
    max_ = max(max_, len(friends))
print(max_)