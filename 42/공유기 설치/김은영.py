import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

min_term, max_term = 1, arr[-1] - arr[0]
answer = 0

while min_term <= max_term:
    last_idx, next_idx = 0, 1
    mid = (min_term + max_term) // 2
    count_machine = 1

    for i in range(1, n):
        if(arr[last_idx] + mid) <= arr[next_idx]:
            count_machine += 1
            last_idx = next_idx
            next_idx = last_idx + 1
        else:
            next_idx += 1

    if count_machine < m:   # 공유기 설치 다 못함
        max_term = mid - 1
    else:     # 공유기 설치 남음
        min_term = mid + 1
        answer = mid


print(answer)