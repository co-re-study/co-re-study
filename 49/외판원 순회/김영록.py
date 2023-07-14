import sys


def tsp(start, current):
    if dist[current][start]:
        return dist[current][start]
    if start == (1 << N)-1:
        if arr[current][0]:
            return arr[current][0]
        else:
            return INF
    ans = INF
    for i in range(1, N):
        if arr[current][i] and not (start >> i) % 2:
            temp = tsp(start | (1 << i), i)
            ans = min(ans, temp+arr[current][i])
    dist[current][start] = ans
    return ans


INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dist = [[0]*(1 << N) for _ in range(N)]
print(tsp(1, 0))