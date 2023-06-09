# 두 노드에서부터 루트 노드까지 올라가면서 카운트
# 공통 부모 만나면 두 카운트 합 출력

import sys
input = sys.stdin.readline

n = int(input())
node1, node2 = map(lambda x: int(x) - 1, input().split())
m = int(input())
parent = list(range(n))
for _ in range(m):
    p, c = map(lambda x: int(x) - 1, input().split())
    parent[c] = p

stack = [(node1, 0), (node2, 0)]
memo = set()
cnt_dict = dict()

answer = -1
while stack:
    node, cnt = stack.pop()
    if node in memo:
        answer = cnt_dict[node] + cnt
        break
    memo.add(node)
    cnt_dict[node] = cnt
    if parent[node] == node:
        continue
    stack.append((parent[node], cnt + 1))

print(answer)



