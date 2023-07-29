# def find_parents(x, y, me):
#     if parents[x] == x:
#         candies[y] += candies[x]
#         candies[x] = 0
#         children[y] += children[x]
#         children[x] = 0
#         parents[x] = y
#         return x
#     return find_parents(parents[x], y, me)
#
#
# n, m, k = map(int, input().split())
# candies = list(map(int, input().split()))
# parents = list(range(n))
# children = [1] * n
# for _ in range(m):
#     s, e = map(int, input().split())
#     s -= 1
#     e -= 1
#     # 아직 둘 다 부모가 없을 때
#     if parents[s] == s and parents[e] == e:
#         parents[e] = s
#         candies[s] += candies[e]
#         candies[e] = 0
#         children[s] += children[e]
#         children[e] = 0
#     # 둘 다 부모 있음 or 왼쪽만 부모 있음
#     elif parents[e] == e or not parents[s] != s and not parents[e] != e:
#         find_parents(s, e, s)
#     # 한 명만 부모 있음
#     elif parents[s] == s:
#         find_parents(e, s, e)
#
# candy_tree = []
# for i in range(n):
#     if candies[i]:
#         candy_tree.append((candies[i], children[i]))
#
# dp = [0] * k
# for c, crying in candy_tree:
#     for i in range(k-1, 0, -1):
#         if crying > i:
#             continue
#         dp[i] = max(dp[i], c + dp[i-crying])
#
# print(max(dp))


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