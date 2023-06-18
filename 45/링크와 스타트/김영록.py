from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
lst = [i for i in range(N)]
gap = sys.maxsize
for i in range(1, N//2+1):
    for a in combinations(range(N), i):
        visited = [0]*N
        for player in a:
            visited[player] = 1
        stat_A = 0
        stat_B = 0
        for j in range(N):
            for k in range(N):
                if visited[j] and visited[k]:
                    stat_A += S[j][k]
                if not visited[j] and not visited[k]:
                    stat_B += S[j][k]
        gap = min(gap, abs(stat_A-stat_B))
print(gap)
