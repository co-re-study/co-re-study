# 아래에 공백이 없이 쌓이는 특성상 각 층의 블록 개수만 알면 될듯하다.
# 각 층마다 필요하거나 제거해야하는 블록 갯수만 안다면 리스트 탐색 한번으로 풀 수 있다.

N, M, B = map(int, input().split())
blocks = [0] * 257
min_height, max_height = 999, 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if max_height < row[j]:
            max_height = row[j]
        if min_height > row[j]:
            min_height = row[j]
        blocks[row[j]] += 1

ans_time = 999999999999999999999999999999
ans_height = 0

for height in range(min_height, max_height + 1):
    inventory = B

    get = sum([x * (idx + 1) for idx, x in enumerate(blocks[height + 1:max_height + 1])])
    put = sum([x * (height - min_height - idx) for idx, x in enumerate(blocks[min_height:height])])

    inventory += get
    if put > inventory:
        continue
    else:
        time = get * 2 + put
        if time <= ans_time:
            ans_time = time
            ans_height = height

print(ans_time, ans_height)
