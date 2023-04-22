import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
stack = []
ans = [-1]*N
for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)
print(*ans)