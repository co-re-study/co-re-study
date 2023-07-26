import sys
from collections import deque
input = sys.stdin.readline

# 원판 돌리기
def rotate(num, direction, rotate_cnt):
    for _ in range(rotate_cnt):
        if direction == 0:
            num_info[num].appendleft(num_info[num].pop())
        else:
            num_info[num].append(num_info[num].popleft())


# 인접한 같은 번호 지우기
def delete_nums():
    # 인접한 같은 번호가 있다면 자리 기억
    delete_positions = set()
    for i in range(N):
        for j in range(M):
            if not num_info[i][j]:
                continue
            if num_info[i][j] in {num_info[i][j - 1], num_info[i][(j + 1) % M]}:
                delete_positions.add((i, j))
            if i > 0 and num_info[i][j] == num_info[i - 1][j]:
                delete_positions.add((i, j))
            if i + 1 < N and num_info[i][j] == num_info[i + 1][j]:
                delete_positions.add((i, j))

    # 기억한 자리가 있다면 지우고 True 반환 / 없다면 False 반환
    flag = False
    for position in delete_positions:
        num_info[position[0]][position[1]] = 0
        flag = True
    return flag


# 평균 맞추기
def adjust_nums():
    acc = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not num_info[i][j]:
                continue
            acc += num_info[i][j]
            cnt += 1
    if not cnt:
        return
    avg = acc / cnt

    for i in range(N):
        for j in range(M):
            if not num_info[i][j]:
                continue
            if num_info[i][j] > avg:
                num_info[i][j] -= 1
            elif num_info[i][j] < avg:
                num_info[i][j] += 1
    return


N, M, T = map(int, input().split())
num_info = [deque(list(map(int, input().split()))) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    # 배수 번호 돌리기
    for n in range(x - 1, N, x):
        rotate(n, d, k)
    # 인접한 번호들 확인하고 지웠는지 확인
    is_deleted = delete_nums()
    # 지웠다면 continue
    if is_deleted:
        continue
    # 인접한 번호들 없다면 평균 맞추기
    adjust_nums()

answer = 0
for i in range(N):
    for j in range(M):
        answer += num_info[i][j]
print(answer)