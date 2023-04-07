def solution(sticker):
    answer = 0

    n = len(sticker)
    if n == 1:  # 1일 수 있음
        return sticker[0]
    dp_1 = [[0, 0, 0] for _ in range(n-1)]
    dp_2 = [[0, 0, 0] for _ in range(n)]
    
    dp_1[0] = [sticker[0], 0, 0]
    dp_2[1] = [sticker[1], 0, 0]

    for i in range(1, n-1):
        dp_1[i] = [max(dp_1[i-1][1], dp_1[i-1][2])+sticker[i], max(dp_1[i-1][0], dp_1[i-1][2]), max(dp_1[i-1][1], dp_1[i-1][2])]
    for i in range(2, n):
        dp_2[i] = [max(dp_2[i-1][1], dp_2[i-1][2])+sticker[i], max(dp_2[i-1][0], dp_2[i-1][2]), max(dp_2[i-1][1], dp_2[i-1][2])]

    answer = max(max(dp_1[-1]), max(dp_2[-1]))

    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
