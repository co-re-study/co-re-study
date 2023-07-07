import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
current_LIS = [num_list[0]]
for i in range(1, N):
    if current_LIS[-1] < num_list[i]:
        current_LIS.append(num_list[i])
    else:
        left = 0
        right = len(current_LIS) - 1
        while left < right:
            mid = (left + right) // 2
            if current_LIS[mid] >= num_list[i]:
                right = mid
            else:
                left = mid + 1
        current_LIS[right] = num_list[i]
print(len(current_LIS))


