N = int(input())
nums = list(map(int, input().split()))

dp = [[0, 0]]  # index도 저장
tracking = [0 for _ in range(N + 1)]
idx = 0

for i in range(len(nums)):
    
    target = nums[i]
    if len(dp) == 1 or dp[-1][0] < target:

        tracking[i] = dp[-1][1]
        dp.append([target, i])
        idx = i
        
    else:
        left, right = 0, len(dp)
        
        while right - left > 1:
            
            mid = (left + right) // 2      
            if dp[mid][0] >= target:
                ans = mid
                right = mid
            else:
                left = mid
    
        dp[ans][0] = target
        dp[ans][1] = i
        tracking[i] = dp[ans - 1][1]
        

ans = []
for _ in range(len(dp) - 1):
    ans.append(nums[idx])
    idx = tracking[idx] 
ans.reverse()
print(len(dp) - 1)
print(*ans)
