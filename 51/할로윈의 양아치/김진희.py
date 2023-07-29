n, m, k = map(int, input().split())
candies = list(map(int, input().split()))
friends = [[] for _ in range(n)]
for _ in range(m):
    s, e = map(int, input().split())
    friends[s - 1].append(e - 1)
    friends[e - 1].append(s - 1)

check = [0] * n  # 방문한 아이는 for문을 돌지 않도록
candy_tree = []

for i in range(n):
    if check[i]:
        continue
    candy = candies[i]
    stack = [i]
    visited = {i}
    check[i] = 1
    while stack:
        now = stack.pop()
        for friend in friends[now]:
            if friend not in visited:
                stack.append(friend)
                visited.add(friend)
                check[friend] = 1
                candy += candies[friend]
    if len(visited) >= k:
        continue
    candy_tree.append((candy, len(visited)))
# print(candy_tree)

dp = [0] * k
for c, crying in candy_tree:
    for i in range(k-1, 0, -1):
        if crying > i:
            continue
        dp[i] = max(dp[i], c + dp[i-crying])

print(dp[k-1])
