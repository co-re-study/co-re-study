from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip('\r\n')


def bfs(start):
    q = deque([start])
    visited = set()
    cnt = 0
    dis = 0
    while q:
        for i in range(len(q)):
            now = q.popleft()
            if now in visited:
                continue
            visited.add(now)
            cnt += dis
            for nxt in friends[now]:
                if nxt in visited:
                    continue
                q.append(nxt)
        dis += 1
    return cnt


n, m = map(int, input().split())
friends = [[] for _ in range(n + 1)]
for i in range(m):
    s, e = map(int, input().split())
    friends[s].append(e)
    friends[e].append(s)

min_value = float('inf')
min_person = 0
for i in range(n):
    cabin = bfs(i + 1)
    if cabin < min_value:
        min_value = cabin
        min_person = i + 1

print(min_person)