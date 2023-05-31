# 이분탐색의 가장 기본이 되는 문제가 아닐까..
# 나무의 높이 시작점과 끝점을 1과 전체 나무의 높이로 시작

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, sum(tree)

while True:
    if start > end:
        break
    # 가운데 값을 잡아주고
    mid = (start + end) // 2
    cnt = 0
    for t in tree:
        # 현재 나무 길이가 중간보다 길면 잘라
        if t > mid:
            cnt += t - mid
    # 완주 했는데 길어? 그럼 시작점 올리고
    if cnt >= m:
        start = mid + 1
    # 아니면 끝점을 내려
    else:
        end = mid - 1

print(end)

