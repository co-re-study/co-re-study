import sys
input = sys.stdin.readline

def find_answer(start_r, start_c, size, is_start, is_end):
    global answer

    # 분할 정복의 시작점이면 "("로 시작
    if is_start:
        answer += "("

    # 0이나 1로만 이루어졌는지 구하기
    flag = False
    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if arr[r][c] != arr[start_r][start_c]:
                flag = True
                break
        if flag:
            break
    else:
        # 0이나 1로만 이루어졌다면 답에 이어 붙이기
        answer += arr[start_r][start_c]
        # 분할 정복의 마지막이면 ")"로 끝내기
        if is_end:
            answer += ")"
        return
    
    # 좌상, 우상, 좌하, 우하 순으로 분할정복
    find_answer(start_r, start_c, size // 2, True, False) # 좌상은 시작점으로
    find_answer(start_r, start_c + size // 2, size // 2, False, False)
    find_answer(start_r + size // 2, start_c, size // 2, False, False)
    find_answer(start_r + size // 2, start_c + size // 2, size // 2, False, True) # 우하는 마지막으로

    # 분할정복 마치고 나왔으면 ")"로 끝내기 (0과 1이 섞인 경우)
    if is_end:
        answer += ")"


N = int(input())
arr = [list(input().strip()) for _ in range(N)]
answer = ""
find_answer(0, 0, N, True, False)
print(answer[1:])