import sys
from heapq import heappush, heappop


def find_root(x):
    if x != roots[x]:
        roots[x] = find_root(roots[x])
    return roots[x]


input = sys.stdin.readline
N = int(input())
planets = [list(map(int, input().split()))+[i] for i in range(N)]
roots = [i for i in range(N)]
planets_x = sorted(planets, key=lambda x: x[0])
planets_y = sorted(planets, key=lambda x: x[1])
planets_z = sorted(planets, key=lambda x: x[2])
queue = []
for i in range(N-1):
    heappush(queue, (abs(planets_x[i][0]-planets_x[i+1]
             [0]), planets_x[i][3], planets_x[i+1][3]))
    heappush(queue, (abs(planets_y[i][1]-planets_y[i+1]
             [1]), planets_y[i][3], planets_y[i+1][3]))
    heappush(queue, (abs(planets_z[i][2]-planets_z[i+1]
             [2]), planets_z[i][3], planets_z[i+1][3]))
ans = 0
while queue:
    l, A, B = heappop(queue)
    if find_root(A) != find_root(B):
        s, e = min(find_root(A), find_root(B)), max(find_root(A), find_root(B))
        roots[e] = s
        ans += l
print(ans)
