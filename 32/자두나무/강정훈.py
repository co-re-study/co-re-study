# 자두를 먹을 때는 떨어질 때 받아먹어야함. 떨어진 자두 X
# 1초마다 두개의 나무 중 하나의 나무에서 열매가 떨어진다.
# 두 개의 나무 중 하나의 나무에서 다른 나무 아래로 빠르게 움직일 수 있음
# 체력 제한 있음
# T= 자두나무에서 자두가 떨어지는 기간
# W = 자두가 움직이는 회수
# 결론: 자두가 받을 수 있는 자두의 최대 개수

# time, chance = map(int, input().split())
# dp = []
# change_index = [0]
# fall_list = [int(input())]
# if fall_list[0] == 1:
#     dp.append(0)
# else:
#     dp.append(1)
# for i in range(1, time):
#     fall_list.append(int(input()))
#     if fall_list[i-1] == fall_list[i]:
#         dp.append(0)
#     else:
#         dp.append(1)
#         change_index.append(i)
#
# max_cnt = 0
# for i in change_index:
#     change_cnt = 0
#     cnt = 0
#     for j in range(i, time):
#
#         if dp[j] == 1:
#             change_cnt += 1
#         if change_cnt == chance+1:
#             break
#         cnt += 1
#     if cnt > max_cnt:
#         max_cnt = cnt
#
# print(max_cnt)
# 최초 나무의 시작이 1인것으로 인해서 터져버림 이런 로직으로 짜려면 조금 더 하드 코딩이 필요할 것 같아서 폐기

T, W = map(int, input().split())
dp = [[0]*(W+1) for _ in range(T+1)]
index_jadu = [0] # 0을 넣는 것은 초기값 및 인덱스 채우기 용이라 의미 딱히 없음.
for i in range(T): # 초당 자두가 떨어지는 리스트를 index_jadu로 만들어줌
    index_jadu.append(int(input()))

# i는 현재 시간(초)를 의미한다.
for i in range(1, T+1):
    #j는 자리를 바꾼 회수를 의미한다.
    for j in range(W+1):
        # j가 0이라는 의미는 자리를 바꾸지 않았다는 의미이다.
        # 따라서, 자두가 떨어지는 위치가 초기값인 1이고, 자리를 바꾸지 않았을 때, +1씩 추가하게 된다.
        # 자두가 떨어지는 위치가 2이면 자두를 먹지 못하기 때문에, 이전과 같다.
        if j == 0:
            if index_jadu[i] == 1:
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0]
        # 이 아래는 사람이 이동을 했다는 의미다. 그렇기 때문에, j, 즉 움직인 회수를 통해서 사람의 위치를 파악할 수 있다.
        else:
            # index_jadu[i] == 1은 자두가 떨어지는 위치가 1이라는 의미이고, j % 2 == 0은 이동한 회수가 짝수번이기 때문에, 1번 위치에 있다는 의미다.
            # index_jadu[i] == 2는 자두가 떨어지는 위치가 2라는 의미이고, j % 2 == 1은 이동한 회수가 홀수번이기 때문에, 2번 위치에 있다는 의미다.
            # 두 가지 경우 모두 자두를 먹을 수 있는 위치에 있다는 공통점이 있다.
            if (index_jadu[i] == 1 and j % 2 == 0) or (index_jadu[i] == 2 and j % 2 == 1):
                # i-1은 현재 시간에서 1초 전의 시간을 의미한다. 즉, 이동을 한번만 할 수 있다는 뜻이다.
                # 이동을 한 번만 할 수 있기 때문에, 현재 시간에서 이동을 한 것과 안한 것 중 더 높은 값을 비교하고, +1을 해주면 된다.
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            # 위에는 자두를 먹을 수 있는 경우였지만, 아래는 자두를 먹을 수 없는 위치에 있다는 특징이 있다.
            # 아래의 경우는 먹지 않고 거르는 게 나을 수 있는 상황이 있기 때문에, 그렇게 저장을 한다.
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
answer = max(dp[-1])

print(answer)