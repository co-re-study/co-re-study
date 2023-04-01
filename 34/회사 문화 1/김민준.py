
#상사가 직속 부하 칭찬히 그 부하는 부하의 직속 부하를 연쇄적으로 칭찬
# 칭찬의 정도를 의미하는 수치가 있는데 이또한 부하들에게 똑같은 칭찬을 받는다

import sys
from collections import defaultdict,deque
input = sys.stdin.readline
n, m = map(int,input().split(' '))

adj = [[] for _ in range(n+1)]
compliment = [0]*(n)
superior = list(map(int,input().split(' ')))

#인접행렬 구하기
for i1 in range(len(superior)):
    adj[i1+1].append(superior[i1])
    adj[superior[i1]].append(i1+1)

children = [[] for _ in range(n+1)]
children_cnt = [0] * (n+1)

stack = [1]
visited = set()
queue = deque([])
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append(destination)
            if(current<destination):
                children[current].append(destination)
                children_cnt[current] += 1
    if not children[current]:
        queue.append(current)
acc = [0]*(n+1)

col_set = set()

for _ in range(m):
    i, w = map(int,input().split(' '))
    col_set.add(i)
    acc[i] += w


for i2 in col_set:
    stack = [i2]
    visited_ans = set()
    w = acc[i2]
    while stack:
        current = stack.pop()
        visited_ans.add(current)
        compliment[current-1] += w
        for destination2 in children[current]:
            stack.append(destination2)

for i3 in compliment:
    print(i3,end=" ")


