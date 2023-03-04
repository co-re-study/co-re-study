import sys
input = lambda : sys.stdin.readline().rstrip('\r\n')


n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

visited = set()
cnt = 0

for i in range(1, n + 1):
    if i not in visited:
        stack = [i]
        while stack:
            now_node = stack.pop()
            if now_node not in visited:
                visited.add(now_node)
                for next_node in adj_list[now_node]:
                    if next_node not in visited:
                        stack.append(next_node)
        cnt += 1

print(cnt)