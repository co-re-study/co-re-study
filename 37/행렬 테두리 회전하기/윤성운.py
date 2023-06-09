def solution(rows, columns, queries):
    
    # 2차원 배열 만들기
    arr = [list(range(i - columns + 1, i + 1)) for i in range(columns, rows * columns + 1, columns)]
    
    # 하, 우, 상, 좌
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    answer = []

    for query in queries:
        r1, c1, r2, c2 = map(lambda x: x - 1, query)
        initial = arr[r1][c1]
        current_r = r1
        current_c = c1
        next_r = r1 + 1
        next_c = c1
        direction = 0
        min_num = initial
        
        # 반시계방향으로 돌기
        while True:
            # 다음 칸 숫자 가져오기
            arr[current_r][current_c] = arr[next_r][next_c]
            if arr[current_r][current_c] < min_num:
                min_num = arr[current_r][current_c]
            
            # 방향 바꾸기
            if direction == 0 and next_r == r2:
                direction = 1
            elif direction == 1 and next_c == c2:
                direction = 2
            elif direction == 2 and next_r == r1:
                direction = 3
            elif direction == 3 and next_c == c1:
                arr[current_r][current_c] = initial
                break
            
            # 좌표 이동
            current_r = next_r
            current_c = next_c
            next_r += dr[direction]
            next_c += dc[direction]
                
        answer.append(min_num)      

    return answer