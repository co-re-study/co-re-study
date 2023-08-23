import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# 누적합
acc_nums = [0] * (N + 1)
for i in range(1, N + 1):
    acc_nums[i] = acc_nums[i - 1] + nums[i]

# multi_acc[i]: 1 ~ i번까지 팀을 골랐을 때의 재미
multi_acc = [0] * (N + 1)
for i in range(1, N + 1):
    multi_acc[i] = multi_acc[i - 1] + (acc_nums[i - 1]) * nums[i]

for _ in range(Q):
    start, end = map(int, input().split())
    print(multi_acc[end] - multi_acc[start - 1] - acc_nums[start - 1] * (acc_nums[end] - acc_nums[start - 1]))
