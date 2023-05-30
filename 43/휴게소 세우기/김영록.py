N, M, L = map(int, input().split())
arr = sorted([0]+list(map(int, input().split()))+[L])
s, e = 1, L-1
ans = 0
while s <= e:
    m = (s+e) // 2
    count = 0
    for i in range(1, N+2):
        count += (arr[i] - arr[i-1]-1)//m
    if count > M: # 더 많이 설치될 때
        s = m+1
    else: # 더 적게 설치될 때 (m을 줄여서 count를 늘리자.)
        e = m-1
        ans = m
print(ans)