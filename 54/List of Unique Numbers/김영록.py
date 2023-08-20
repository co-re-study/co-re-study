N = int(input())
nums = list(map(int, input().split()))
ans = 0
s, e = 0, 0
visited = [0]*100001
while s < N and e < N:
    if not visited[nums[e]]:
        visited[nums[e]] = 1
        e += 1
        ans += e-s
    else:
        while visited[nums[e]]:
            visited[nums[s]] = 0
            s += 1
print(ans)
