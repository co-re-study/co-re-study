import sys
input=sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]

boat_cnt = 0
for i in range(1, N):
    if arr[i] == 0:
        continue
    # 인덱스 1번부터 시작
    current_diff = arr[i] - arr[0]
    answer_candi = 1
    for j in range(1, N):
        if arr[j] == 0:
            continue
        # 기념일로 적어 놓은 날이 현재 기록한 간격만큼 된다면 같은 배로 취급하여 배열에서 0으로 만든다.
        if arr[j] % current_diff == 1:
            answer_candi += current_diff
            arr[j] = 0
    # answer_candi값에 변화가 있다면 바로 기록해버린다.
    if answer_candi != 1:
        boat_cnt += 1

print(boat_cnt)