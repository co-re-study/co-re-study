import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

num_set = set()
left = 0
right = 0
answer = 0

# 윈도우의 오른쪽 인덱스를 늘리면서 중복되지 않으면 윈도우 크기만큼 더하기
# 만약 중복이라면 중복이 안 될 때까지 왼쪽 인덱스 늘리기
while right < N:
    while left < right and nums[right] in num_set:
        num_set.remove(nums[left])
        left += 1

    num_set.add(nums[right])
    answer += right - left + 1
    right += 1    
        
print(answer)