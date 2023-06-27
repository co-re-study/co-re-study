import sys
input = sys.stdin.readline

input() # 첫 input 버리기
nums = sorted(list(set(map(int, input().split())))) # 중복 제거
N = len(nums) # 중복 제거한 새로운 N 저장

# nums = [0] 이면 1 출력
if not nums[0] and N == 1:
    print(1)
    exit(0)

# nums에 0 없으면 0 출력
if nums[0]:
    print(0)
    exit(0)

# 0부터 보다가 없는 수 발견하면 break
answer = 0
for num in nums:
    if answer != num:
        break
    answer += 1

print(answer + 2)