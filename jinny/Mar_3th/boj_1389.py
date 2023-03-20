# 케빈 베이컨의 6단계 법칙
from collections import deque
n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

answer = 0
bacon = [99999] + [0] * n

for i in range(1, n + 1):      # 본인
    for j in range(1, n + 1):  # 친구
        if i == j:
            continue
        q = deque()
        visited = set()
        q.append(i)
        visited.add(i)
        flag = 1
        while q and flag:
            bacon[i] += 1
            for bfs in range(len(q)):
                if flag:
                    node = q.popleft()
                    for z in range(1, n + 1):
                        if arr[node][z] and z == j:
                            flag = 0
                            break
                        elif arr[node][z] and z not in visited:
                            q.append(z)
                            visited.add(z)
                else:
                    break
    else:
        if bacon[i] < bacon[answer]:
            answer = i
print(answer)