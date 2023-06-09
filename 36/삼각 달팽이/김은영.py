def solution(n):
    # 삼각형은 왼쪽 아래 방향으로 갔다가 오른쪽으로 일직선으로 갔다가 왼쪽 위로 올라오는경우가 다임
    # 달팽이 문제 삼각형 버전
    dy = [1, 0, -1]
    dx = [0, 1, -1]
    tri = []
    for i in range(1, n+1):
        temp = [0] * i
        tri.append(temp)
    answer = []
    num = 1
    dir = 0
    y, x = 0, 0
    while num <= n*(n+1)//2:
        tri[y][x] = num
        if 0 <= x+dx[dir] < n and 0 <= y+dy[dir] < n and (not tri[y + dy[dir]][x + dx[dir]]):
            y, x = y + dy[dir], x + dx[dir]
        else:
            dir += 1
            dir %= 3
            y, x = y + dy[dir], x + dx[dir]
        num += 1
    for i in range(n):
        for j in range(i + 1):
            answer.append(tri[i][j])
    return answer