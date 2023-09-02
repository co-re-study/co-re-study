n, m, l, s = map(int, input().split())
stars = list(tuple(map(int, input().split())) for _ in range(s))
answer = 0
# 첫번째 별과
for i in range(s):
    # 두번째 별을 지정해서 최소 별 하나를 포함하는 네 구역을 탐색
    for j in range(s):
        acc = 0
        # 구역 안에 몇 개의 별이 있는지 탐색
        for k in range(s):
            if stars[i][0] <= stars[k][0] <= stars[i][0]+l \
                    and stars[j][1] <= stars[k][1] <= stars[j][1]+l:
                acc += 1
        answer = max(answer, acc)
print(s - answer)