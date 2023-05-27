import sys
input = sys.stdin.readline

N, C = map(int, input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

left = 1
right = nums[-1]
answer = -1
while left <= right:
    middle = (left + right) // 2

    idx = 0
    cnt = 1
    next_idx = 1

    while idx < N and next_idx < N:
        while nums[idx] + middle > nums[next_idx]:
            next_idx += 1
            if next_idx == N:
                break
        else:
            cnt += 1
            idx = next_idx
            next_idx += 1
            if cnt == C and answer < middle:
                answer = middle
                break
    else:
        right = middle - 1
        continue
    left = middle + 1

print(answer)
