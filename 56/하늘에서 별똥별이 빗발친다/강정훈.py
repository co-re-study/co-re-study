# 시간 복잡도 상으로 N, M 배열을 만들어서 브루트포스로 다 돌면 무조건 시간초과.

# 별똥별 인풋이 비교적 작기 때문에, 별똥별 간의 거리 비교를 통해 알아내는 게 좋다는 생각 구현
N, M, L, K = map(int, input().split())

meteo_list = [list(map(int, input().split())) for _ in range(K)]
tramperlin_cnt = 0
for i in range(K):
    for j in range(K):
        cnt = 0
        for k in range(K):
            if meteo_list[i][0] <= meteo_list[k][0] <= meteo_list[i][0] + L and meteo_list[j][1] <= meteo_list[k][1] <= meteo_list[j][1] + L:
                cnt += 1
        tramperlin_cnt = max(tramperlin_cnt, cnt)
answer = K-tramperlin_cnt
print(answer)
