import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_height = -1
min_height = 257

# key: 높이, value: 해당 높이 개수
height_dict = dict()

# 최대 높이, 최소 높이, 각 높이 당 개수 구하기
for r in range(N):
    for c in range(M):
        if arr[r][c] > max_height:
            max_height = arr[r][c]
        if arr[r][c] < min_height:
            min_height = arr[r][c]
        
        if arr[r][c] in height_dict:
            height_dict[arr[r][c]] += 1
        else:
            height_dict[arr[r][c]] = 1

min_time = 987654321
answer_height = 0

# 모든 높이 보기
for height in range(min_height, max_height + 1):

    amount_to_fill = 0
    amount_to_dig = 0

    # 해당 높이에서 채워야 하는 양과 파내야 하는 양 비교
    for h in height_dict:
        if h > height:
            amount_to_dig += (h - height) * height_dict[h]
        elif h < height:
            amount_to_fill += (height - h) * height_dict[h]

    time = amount_to_dig * 2 + amount_to_fill

    if time <= min_time and B + amount_to_dig >= amount_to_fill:
        min_time = time
        answer_height = height
    
print(min_time, answer_height)
