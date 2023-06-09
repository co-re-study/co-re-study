import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))

answer = 0
acc = 0
for num in nums:
    acc += num
    answer += acc

print(answer)