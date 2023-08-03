import sys
from collections import deque
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    prisoners = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == "$":
                prisoners.append([i, j, 0, 0])

    INF = 987654321
    # deque 두 개 관리
    # 첫 번째 deque: 1번 죄수, 두 번째 deque: 2번 죄수
    # 각 deque는 [열, 행, 연 문의 수, 상대 죄수 만났는지 여부]로 구성
    deque_list = [deque([prisoners[0]]), deque([prisoners[1]])]
    # distances는 [1번 죄수가 연 문의 개수, 2번 죄수가 연 문의 개수, 1번 혼자 + 2번 혼자 + 같이 연 문의 개수]로 구성
    distances = [[[INF] * 3 for i in range(M)] for j in range(N)]
    distances[prisoners[0][0]][prisoners[0][1]][0] = 0
    distances[prisoners[1][0]][prisoners[1][1]][1] = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    current_prisoner = 0

    # 두 죄수 중 한 죄수라도 움직일 수 있다면 움직이기
    while deque_list[0] or deque_list[1]:
        # 죄수 번갈아가면서 bfs
        current_prisoner = (current_prisoner + 1) % 2
        if not deque_list[current_prisoner]:
            continue
        for _ in range(len(deque_list[current_prisoner])):
            current = deque_list[current_prisoner].popleft()
            if current[0] in {0, N - 1} or current[1] in {0, M - 1}:
                continue

            for i in range(4):
                nr = current[0] + dr[i]
                nc = current[1] + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    # 문을 만났을 때
                    if arr[nr][nc] == "#":
                        # 혼자 문 열기
                        if current[2] + 1 < distances[nr][nc][current_prisoner]:
                            deque_list[current_prisoner].append((nr, nc, current[2] + 1, current[3]))
                            distances[nr][nc][current_prisoner] = current[2] + 1
                        # 상대 죄수가 열었던 문에 처음 합류했으면 내가 혼자 연 문에 상대 죄수가 혼자 열었던 문 더하기
                        if not current[3] and distances[nr][nc][(current_prisoner + 1) % 2] != INF and current[2] + distances[nr][nc][(current_prisoner + 1) % 2] < distances[nr][nc][2]:
                            deque_list[current_prisoner].append((nr, nc, current[2] + distances[nr][nc][(current_prisoner + 1) % 2], 1))
                            distances[nr][nc][2] = current[2] + distances[nr][nc][(current_prisoner + 1) % 2]
                        # 상대 죄수와 이미 합류했었다면 같이 문 열기
                        elif current[3] and current[2] + 1 < distances[nr][nc][2]:
                            deque_list[current_prisoner].append((nr, nc, current[2] + 1, 1))
                            distances[nr][nc][2] = current[2] + 1
                    # 문 안 열고도 갈 수 있을 때
                    elif arr[nr][nc] not in {"#", "*"}:
                        # 혼자 가기
                        if current[2] < distances[nr][nc][current_prisoner]:
                            deque_list[current_prisoner].appendleft((nr, nc, current[2], current[3]))
                            distances[nr][nc][current_prisoner] = current[2]
                        # 상대 죄수와 합류했었다면 같이 가기
                        if current[3] and current[2] < distances[nr][nc][2]:
                            deque_list[current_prisoner].appendleft((nr, nc, current[2], 1))
                            distances[nr][nc][2] = current[2]

    # 각 모서리 값 보면서 최소 구하기
    answer = INF
    min_A = INF
    min_B = INF
    for i in range(N):
        answer = min(answer, distances[i][0][2], distances[i][M - 1][2])
        min_A = min(min_A, distances[i][0][0], distances[i][M - 1][0])
        min_B = min(min_B, distances[i][0][1], distances[i][M - 1][1])
    for i in range(M):
        answer = min(answer, distances[0][i][2], distances[N - 1][i][2])
        min_A = min(min_A, distances[0][i][0], distances[N - 1][i][0])
        min_B = min(min_B, distances[0][i][1], distances[N - 1][i][1])

    # 둘이 같이 나간 것과 따로 나간 것 중 최소 구하기
    answer = min(answer, min_A + min_B)

    print(answer)
        
