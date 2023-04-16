def changeDirection(direction):
    if direction == 2:
        return 0
    else:
        return direction + 1

def solution(n):
    answer = []
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    snare = [[0]*(i+1) for i in range(n)]
    k = 0
    r, c = 0, 0
    snare[r][c] = 1
    direction = 0
    while k < ((n+1)*n)//2:
        k += 1
        nr = r + dr[direction]
        nc = c + dc[direction]
        if nr >= n or nc >= n or snare[nr][nc] != 0:
            direction = changeDirection(direction)
            nr = r + dr[direction]
            nc = c + dc[direction]
        snare[r][c] = k
        r = nr
        c = nc

    for i in range(len(snare)):
        answer += snare[i]
    return answer
print(solution(6))