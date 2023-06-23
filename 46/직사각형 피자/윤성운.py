import sys
input = sys.stdin.readline

# 피자 자르기 (중복되는 길이는 한번만 저장하고 딕셔너리에 그 개수 저장)
def cutting(cutting_points, total_length):
    length_list = []
    length_dict = dict()
    current_height = 0
    for i in range(len(cutting_points)):
        current_size = cutting_points[i] - current_height
        if current_size in length_dict:
            length_dict[current_size] += 1
        else:
            length_list.append(current_size)
            length_dict[current_size] = 1
        current_height = cutting_points[i]
    last_length = total_length - current_height
    if last_length in length_dict:
        length_dict[last_length] += 1
    else:
        length_list.append(last_length)
        length_dict[last_length] = 1
    return length_list, length_dict


W, H, K = map(int, input().split())
N = int(input())
y_cutting_points = list(map(int, input().split()))
M = int(input())
x_cuttings_points = list(map(int, input().split()))

# length_list: 현재 자른 길이들
# length_dict: key: 자른 길이, value: 해당 길이 개수
y_length_list, y_length_dict = cutting(y_cutting_points, H)
x_length_list, x_length_dict = cutting(x_cuttings_points, W)
y_length_list.sort()

# 현재 길이보다 작거나 같은 길이 개수 누적해서 저장
y_acc_list = []
acc = 0
for length in y_length_list:
    acc += y_length_dict[length]
    y_acc_list.append(acc)

# 이분탐색
answer = 0
for length in x_length_list:
    if length * y_length_list[0] > K:
        continue
    left = 0
    right = len(y_length_list) - 1
    max_idx = 0
    while left <= right:
        middle = (left + right) // 2
        if y_length_list[middle] * length <= K:
            left = middle + 1
            max_idx = middle # 최대 길이 저장
        else:
            right = middle - 1
    answer += x_length_dict[length] * y_acc_list[max_idx]

print(answer)
