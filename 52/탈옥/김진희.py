from collections import deque


def bfs(x, y):
    global answer

    # 가장 작은 수를 계속 진행 or 기록하기 위해 최소값을 먼저 뽑을 것
    q = deque([(x, y)])
    # 얘가 곧 visited
    cnt = [[-1] * w for _ in range(h)]
    cnt[x][y] = 0  # 잊지 말고 시작점 체크

    while q:
        cr, cc = q.popleft()              # 최소값을 항상 맨 앞에 저장하고 맨 앞을 뽑는다
        for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < h and 0 <= nc < w and cnt[nr][nc] == -1:  # 이미 적힌 게 빨리 뽑아서 온 최소값일 것, 재방문은 뒤에 있던 큰 수일 테니까
                if arr[nr][nc] == '#':    # 문을 열면 +1이 되므로 뒤에 추가하고
                    q.append((nr, nc))
                    cnt[nr][nc] = cnt[cr][cc] + 1
                elif arr[nr][nc] == '.':  # 문이 아니면 추가금이 없으므로 앞에 추가
                    q.appendleft((nr, nc))
                    cnt[nr][nc] = cnt[cr][cc]
    return cnt


for tc in range(1, int(input()) + 1):
    h, w = map(int, input().split())  # 2 ~ 100

    # [0] 바깥을 둘러싼 감옥 만들기
    arr = [['.'] * (w + 2)] + [['.'] + list(input()) + ['.'] for _ in range(h)] + [['.'] * (w + 2)]
    h, w = h + 2, w + 2

    # [1] 죄수 위치 찾기
    people = []
    doors = set()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '$':
                people.append((i, j))
                arr[i][j] = '.'  # 죄수 자리 .으로

    # [2] 죄수 간의 최단거리 + 바깥과의 최단거리를 구할 것
    # 각각 죄수1, 죄수2, 바깥(0, 0)에서 출발한 모든 자리를 문 몇 개 열고 갈 수 있는 지 기록
    arr1 = bfs(people[0][0], people[0][1])
    arr2 = bfs(people[1][0], people[1][1])
    arr3 = bfs(0, 0)

    # [3] 공간 별로 서로 문을 몇 개 열고 왔는지 합친다.
    # 단, 공간이 문이면 모두 세 곳에서 열었으므로 두 번을 빼준다.
    # 셋이 만난 수 중 가장 작은 수가 답
    answer = 99999
    for i in range(h):
        for j in range(w):
            # 아무도 못 가게 벽으로 둘러쌓인 곳은 -1로 남아있어서 제외해야함
            if -1 not in {arr1[i][j], arr2[i][j], arr3[i][j]}:
                if arr[i][j] == '#':
                    answer = min(answer, arr1[i][j] + arr2[i][j] + arr3[i][j] - 2)
                elif arr[i][j] == '.':
                    answer = min(answer, arr1[i][j] + arr2[i][j] + arr3[i][j])
    print(answer)