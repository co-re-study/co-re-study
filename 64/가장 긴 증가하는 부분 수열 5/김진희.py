# 가장 긴 증가하는 부분수열 5
def binary_search(x):
    start = 0
    end = len(dp) - 1
    while start < end:
        middle = (start + end) // 2
        if dp[middle] < x:
            start = middle + 1
        else:
            end = middle
    idx.append((end, x))
    dp[end] = x


n = int(input())
a = list(map(int, input().split()))
dp = [-9000000000, a[0]]
idx = [(1, a[0])]
for i in range(1, n):
    if a[i] > dp[-1]:
        idx.append((len(dp), a[i]))
        dp.append(a[i])
    else:
        binary_search(a[i])

answer = []
cnt = len(dp) - 1
for index, item in idx[::-1]:
    if index == cnt:
        answer.append(item)
        cnt -= 1
        if not cnt:
            break

print(len(dp) - 1)
print(*answer[::-1])