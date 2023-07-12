import sys
input = sys.stdin.readline

N = int(input())
S = input()

max_cnt = 0

# 0: 아직 시작x, 1: (로 시작, 2: )로 시작
# max_cnt: 가장 내부에 있는 괄호 쌍의 depth
status = 0
cnt = 0
for char in S:
    if char == "(":
        if not status:
            status = 1
            cnt = 1
            max_cnt = max(cnt, max_cnt)
        elif status == 1:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt -= 1
            if not cnt:
                status = 0

    if char == ")":
        if not status:
            status = 2
            cnt = 1
            max_cnt = max(cnt, max_cnt)
        elif status == 1:
            cnt -= 1
            if not cnt:
                status = 0
        else:
            cnt += 1
            max_cnt = max(cnt, max_cnt)

# 괄호 묶음이 제대로 끝난 경우에만 답 출력
if not status:
    print(max_cnt)
else:
    print(-1)
        
