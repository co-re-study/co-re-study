import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

nums = [int(input()) for _ in range(N)]
nums += nums[:k + 1] # 초밥 연장하기

current = deque(nums[:k]) # 현재 고른 초밥들
cnt_dict = dict() # 초밥 번호마다 현재 몇 개를 골랐는지 기록
max_cnt = 0
for num in nums[:k]:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1
        max_cnt += 1

# 쿠폰 초밥은 무조건 하나가 들어있는 상태
if c in cnt_dict:
    cnt_dict[c] += 1
else:
    cnt_dict[c] = 1
    max_cnt += 1

current_cnt = max_cnt # 현재 고른 초밥 종류 개수

# 슬라이딩 윈도우
for i in range(N):
    left = current.popleft() 
    right = nums[i + k]
    current.append(right)
    
    cnt_dict[left] -= 1
    if not cnt_dict[left]:
        current_cnt -= 1
    if right in cnt_dict:
        if not cnt_dict[right]:
            current_cnt += 1
        cnt_dict[right] += 1
    else:
        cnt_dict[right] = 1
        current_cnt += 1

    if current_cnt > max_cnt:
        max_cnt = current_cnt
    
print(max_cnt)

