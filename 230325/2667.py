from collections import defaultdict, deque
import sys
input = lambda : sys.stdin.readline().rstrip('\r\n')


def bfs(x, y):
    global numbers
    q = deque([(x, y)])                 # queue를 저장할 변수
    dr = [0, 1, 0, -1]                  # 사방 탐색을 하기위한 변수
    dc = [-1, 0, 1, 0]                  # 탐색 순서는 상우하좌

    while q:
        r, c = q.popleft()              # 집의 좌표 뽑아옴
        if (r, c) in visited:           # 방문한 좌표면
            continue                    # 다음 좌표
        visited.add((r, c))             # 방문한 좌표에 추가
        count[numbers] += 1             # 해당하는 단지의 집의 개수 +1
        for k in range(4):              # 사방탐색
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n and map[nr][nc] == 1:    # map의 범위 내에 있고 집이 있는 좌표라면
                q.append((nr, nc))                                  # queue에 추가

    numbers += 1                                                    # 단지 번호 +1


n = int(input())
map = [[0] * n for _ in range(n)]        # n * n 배열 만들기
house_point = set()                     # 집이 있는 좌표를 저장할 set
for i in range(n):
    line = list(input())                # 한줄씩 입력 받아 list로 만듦
    for j in range(n):
        if line[j] == '1':              # '1' 이면 해당하는 map의 값을 1로
            map[i][j] = 1
            house_point.add((i, j))     # 집이 있는 좌표를 넣어줌
        else:
            map[i][j] = 0               # '1'이 아니면 해당하는 map의 값을 0으로

count = defaultdict(int)                # 단지의 수와 각 단지의 집의 수를 저장할 변수
visited = set()                         # 방문한 곳을 저장할 변수
numbers = 1                             # 단지의 번호를 저장할 변수
for x, y in house_point:                # 집이 있는 좌표를 하나씩 꺼내서
    if (x, y) not in visited:           # 방문한 곳이 아니라면
        bfs(x, y)                       # bfs 탐색

print(len(count))                       # 단지의 수
for i in sorted(count.values()):        # 집의 개수 오름차순
    print(i)                            # 출력