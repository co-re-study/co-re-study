N = int(input())

default = list(map(int, input().split()))
str = list(map(int, input().split()))
diff = [str[i+1]-str[i] for i in range(N-1)] + [0]

start = 0
for i in range(N):
    start += default[i] * str[i]

D = int(input())

dp = [[default[:], 0] for _ in range(N)]

for _ in range(D):
    new_dp = []

    for i in range(N):
        last = -1
        target = -float('INF')

        for j in range(N):
            if (i==N-1 or dp[j][0][i]) and target < dp[j][1] + diff[i]:
                last = j
                target = dp[j][1] + diff[i]
        
        update = dp[last][0][:]

        if i != N-1 and last != -1:
            update[i] -= 1
            update[i+1] += 1
            new_dp.append([update, dp[last][1]+diff[i]])
        else:
            new_dp.append([update, dp[last][1]])
        print(new_dp)
    dp = new_dp
    print(dp)

answer = 0
for i in range(N):
    answer = max(answer, dp[i][1])

print(answer + start)