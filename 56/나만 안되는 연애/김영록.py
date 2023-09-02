import sys
input = sys.stdin.readline


def find_root(x):
    if x != nums[x]:  # 루트 찾아야 하는 경우 (그냥 자기가 루트면 찾을 필요x)
        nums[x] = find_root(nums[x])  # 계속 들어가자
    return nums[x]


N, M = map(int, input().split())
nums = [i for i in range(N+1)]
college = ['O']+list(input().split())
routes = [list(map(int, input().split())) for _ in range(M)]
routes.sort(key=lambda x: (x[2], x[0], x[1]))
ans = 0
temp = 0
for route in routes:
    u, v, d = route
    if college[u] != college[v] and find_root(u) != find_root(v):
        ans += d
        temp += 1
        s, e = min(find_root(u), find_root(v)), max(
            find_root(u), find_root(v))
        nums[e] = s
    if temp == N-1:
        break
print(ans if temp == N-1 else -1)
