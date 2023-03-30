import sys

n, m = map(int, sys.stdin.readline().split())
parent_info = list(map(int, sys.stdin.readline().split()))

# 트리 만들기
parent = [0] * n
children = [[] for _ in range(n)]
for i in range(1, n):
    parent[i] = parent_info[i] - 1
    children[parent_info[i] - 1].append(i)

# 칭찬 받은 사원 정보 저장
praise_memo = [0] * n
for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    praise_memo[i - 1] += w

# 칭찬 받은 사원부터 자손 노드 모두 칭찬하기
answer = [0] * n
for node in range(1, n):
    if not praise_memo[node]:
        continue
    stack = children[node][:]
    answer[node] += praise_memo[node]
    while stack:
        current = stack.pop()
        answer[current] += praise_memo[node]
        stack.extend(children[current])

print(" ".join(map(str, answer)))

