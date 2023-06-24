import sys
input=sys.stdin.readline
N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
travel_plan = list(map(int, input().split()))
root = [i for i in range(N+1)]

def union(x, y):
    x = find(x)
    y = find(y)
    root[x] = root[y]

def find(x):
    if root[x] != x:
        return find(root[x])
    else:
        return root[x]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            if find(i+1) != find(j+1):
                union(find(i+1), find(j+1))

answer = find(travel_plan[0])
flag = True
for i in range(1, len(travel_plan)):
    if answer != find(travel_plan[i]):
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")

