W, H, K = map(int, input().split())

N = int(input())
horizontal = [0] + list(map(int, input().split())) + [H]
M = int(input())
vertical = [0] + list(map(int, input().split())) + [W]

x_list = []
y_list = []
for i in range(1, N+2):
    x_list.append(horizontal[i] - horizontal[i-1])
for j in range(1, M+2):
    y_list.append(vertical[j] - vertical[j-1])

x_list.sort()
y_list.sort()
answer = 0
for x_len in x_list:
    left, right = 0, M
    if x_len * y_list[left] > K:
        continue
    if x_len * y_list[right] <= K:
        answer += M+1
        continue
    while left <= right:
        mid = (left + right) // 2
        if x_len * y_list[mid] > K:
            right = mid - 1
        else:
            max_idx = mid
            left = mid + 1
    answer += max_idx + 1

print(answer)

