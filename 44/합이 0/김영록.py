from collections import Counter
N = int(input())
arr = sorted(list(map(int, input().split())))
num_cnt = Counter(arr)
ans = 0
for s in range(N-2):
    f = arr[s]
    m, e = s+1, N-1
    while m < e:
        temp = f + arr[m] + arr[e]
        if temp == 0:
            if arr[m] == arr[e]:
                ans += e-m
            else:
                ans += num_cnt[arr[e]]
            m += 1
        elif temp < 0:
            m += 1
        else:
            e -= 1
print(ans)
'''
m의 개수
e의 개수
'''