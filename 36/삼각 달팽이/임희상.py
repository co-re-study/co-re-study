def solution(n):
    answer = []
    snail = []
    for i in range(n):
        snail.append([0]*(i+1))
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    d = 0
    current = [0, 0]
    final = n*(n+1)//2
    for num in range(1, final+1):
        r, c = current
        snail[r][c] = num
        if 0 <= r+dr[d] < n and 0 <= c+dc[d] < n and not snail[r+dr[d]][c+dc[d]]:
            current = [r+dr[d], c+dc[d]]
        else:
            d += 1
            d %= 3
            current = [r+dr[d], c+dc[d]]
    
    for i in range(n):
        answer.extend(snail[i])
        
    return answer