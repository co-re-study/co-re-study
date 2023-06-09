import sys

input = sys.stdin.readline
N, M, B = map(int, input().split())

# 배열이 굳이 2차원으로 표현되었을 뿐 답을 구하는데 2차원일 필요는 없음.
ground_list = []
for i in range(N):
    ground_list += list(map(int, input().split()))

min_block = 9999999999999999999999999
max_block = 0
sum_block = 0

# 블럭들의 최대 높이, 최소 높이, 블럭들의 합을 구한다.
# 최대 높이와 최소 높이를 통해 높이 탐색 범위를 줄여주고, 블럭들의 합을 이용해서 블럭을 넣을지 뺄지 판단한다.
for i in range(len(ground_list)):
    if ground_list[i] > max_block:
        max_block = ground_list[i]
    if ground_list[i] < min_block:
        min_block = ground_list[i]
    sum_block += ground_list[i]

min_time = 9999999999999999999999999
answer = ground_list[0]

# 최대 높이에서 최소 높이로 내려가면서 탐색해준다.
for current_height in range(max_block, min_block - 1, -1):
    if sum_block + B >= current_height * N * M:
        time = 0
        # 현재 탐색중인 높이와 블럭의 높이를 비교하고 블럭을 넣거나 뺀다.
        for block_height in ground_list:
            height_difference = block_height - current_height
            # 현재 높이에서 부족한만큼 블럭 넣기
            if height_difference > 0:
                time += height_difference * 2
            # 현재 높이에서 남는 만큼 블럭 빼기
            elif height_difference < 0:
                time -= height_difference
        # 정답 갱신 // 최소 시간과 높이
        if time < min_time:
            min_time = time
            answer = current_height

print(min_time, answer)