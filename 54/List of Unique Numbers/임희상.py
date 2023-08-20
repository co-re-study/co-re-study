N = int(input())
nums = list(map(int, input().split()))
left = right = 0
answer = 0
current = set()

while right < N:

    while left < right:
        if nums[right] not in current:
            break
        current.discard(nums[left])
        left += 1
        
    current.add(nums[right])
    answer += right - left + 1
    right += 1

print(answer)