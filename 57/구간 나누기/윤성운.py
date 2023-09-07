import sys
input = sys.stdin.readline

def dfs(current, depth, acc):
    if memo[depth][current] >= acc:
        return
    memo[depth][current] = acc

    if current >= N:
        return
    
    if depth >= M:
        return
    
    for end in range(current, N):
        tmp = acc + acc_nums[end + 1] - acc_nums[current]
        if end + 2 >= N:
            if memo[depth + 1][N] >= tmp:
                continue
            memo[depth + 1][N] = tmp
        for next in range(end + 2, N):
            if memo[depth + 1][next] < tmp:
                dfs(next, depth + 1, tmp)


N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]

acc_nums = [0] * (N + 1)
acc = 0
for i in range(N):
    acc += nums[i]
    acc_nums[i + 1] = acc

memo = [[-987654321] * (N + 1) for _ in range(M + 1)]
for i in range(N):
    dfs(i, 0, 0)
print(max(memo[-1]))