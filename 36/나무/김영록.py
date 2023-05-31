# 시간 효율화를 위해 Counter를 사용했다.
# Counter는 각 문자가 문자열에서 몇 번씩 나타나는지를 알려주는 객체를 반환시켜준다.
# Counter 미사용시 2932ms Counter 사용시 432ms (python3 기준)
from collections import Counter
N, M = map(int, input().split())
lst = Counter(map(int, input().split()))
left, right = 1, max(lst)
# 이분탐색
while left <= right:
    mid = (left+right)//2
    sum_cut = 0
    for i, j in lst.items():
        if i-mid > 0:
            sum_cut += (i-mid)*j
            if sum_cut > M:
                break
    if sum_cut < M:
        right = mid-1
    else:
        left = mid+1
print(right)
