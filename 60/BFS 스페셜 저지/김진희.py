def solve():
    global answer
    idx = 1

    visited = [0] * (N + 1)
    visited[1] = 1
    for current in result:
        group = set()
        for nr in arr[current]:
            if not visited[nr]:
                visited[nr] = 1
                group.add(nr)

        for check in range(idx, idx + len(group)):
            if result[check] not in group:
                answer = 0
                return
            idx += 1


N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
result = list(map(int, input().split()))

answer = 1
if result[0] != 1:
    answer = 0
else:
    solve()
print(answer)
