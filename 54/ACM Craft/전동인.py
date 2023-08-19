from collections import deque

t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    next_build = [[] for _ in range(n+1)]
    pre_cnt = [0] * (n+1)  # 선행 건설 카운트
    min_time = [0] * (n+1)

    for _ in range(k):
        i, j = map(int, input().split())
        next_build[i].append(j)
        pre_cnt[j] += 1  # 다른 다음 루트로 삼는 경우, 카운트 업

    queue = deque()

    for i in range(1, n+1):
        if pre_cnt[i] == 0:
            queue.append(i)
            min_time[i] = build_time[i]

    while queue:
        current = queue.popleft()

        for next in next_build[current]:
            pre_cnt[next] -= 1
            min_time[next] = max(
                min_time[next], min_time[current] + build_time[next])

            if pre_cnt[next] == 0:
                queue.append(next)

    w = int(input())
    print(min_time[w])
