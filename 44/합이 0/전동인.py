# 입력
n = int(input())
nums = list(map(int, input().split()))
# 정렬
nums.sort()

cnt = 0

for i in range(n-2):  # 첫 요소 고정
    l, r = i + 1, n - 1  # 투 포인터 설정
    while l < r:
        total = nums[i] + nums[l] + nums[r]
        if total < 0:  # 합이 0보다 작으면 왼쪽 포인터 이동
            l += 1
        elif total > 0:  # 합이 0보다 크면 오른쪽 포인터 이동
            r -= 1
        else:
            if nums[l] == nums[r]:
                cnt += (r - l + 1)*(r - l)//2
                break
            else:
                l_count = 1
                while l + 1 < r and nums[l] == nums[l + 1]:
                    l += 1
                    l_count += 1
                r_count = 1
                while l < r - 1 and nums[r] == nums[r - 1]:
                    r -= 1
                    r_count += 1
                cnt += l_count * r_count
                l += 1
                r -= 1


print(cnt)
