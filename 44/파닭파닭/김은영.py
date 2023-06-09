# 임이의 파 길이를 정해놓고 이분탐색
# start = 1 로 두니 pass 0 은 시간초과

n, m = map(int, input().split())
par = [int(input()) for _ in range(n)]

answer = 0
start = 1
end = max(par)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    if not mid:
        continue
    for i in par:
        cnt += (i // mid)
    if cnt < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(sum(par) - answer * m)