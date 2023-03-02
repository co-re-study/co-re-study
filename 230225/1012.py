for _ in range(int(input())):
    m, n, y = map(int, input().split())

    # 배추 위치 파악
    targets = []
    for _ in range(y):
        r, c = map(int, input().split())
        targets.append((r, c))

    # 베추의 위치로 부터 사방탐색
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = set()
    cnt = 0
    for x, y in targets:                            # 배추의 위치 하나를 가져옴
        if (x, y) not in visited:                   # 방문한 곳이 아니면
            stack = [(x, y)]                        # 스택에 추가
            while stack:                            # 스택이 다 빌때까지 반복
                r, c = stack.pop()                  # 스택에 담긴 배추의 좌표 하나 가져옴
                if (r, c) not in visited:           # 방문한 곳이 아니면
                    visited.add((r, c))             # 방문한 곳으로 표시
                    for k in range(4):              # 사방탐색
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if (nr, nc) in targets:     # 사방탐색에 인접한 배추가 있으면
                            stack.append((nr, nc))  # 스택에 추가
            cnt += 1                                # 더 이상 인접한 배추가 없으면 배추벌레 개수 +1

    print(cnt)