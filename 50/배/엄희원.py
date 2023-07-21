N = int(input())

arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)

ans = 0
memo = [0] * N
cnt = 1

for i in range(1, N):
    if cnt == N:
        break
    dist = arr[i] - arr[0]

    flag = False
    for j in range(i, N):
        if memo[j] == 0 and arr[j] % dist == 1:
            memo[j] = 1
            cnt += 1
            flag = True
    if flag:
        ans += 1

print(ans)







