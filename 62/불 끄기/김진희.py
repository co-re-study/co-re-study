'''
첫 줄부터 전부 다 눌러보기
다만 둘째줄부턴 위칸이 눌려있을 때만 누르기
'''


def solve(k):
    global answer

    table = [arr[i][:] for i in range(10)]
    cnt = 0
    # 경우의 수에 맞춰 실제로 눌러줌
    k = str(bin(k))[2:]
    k = '0'*(10-len(k)) + k
    for on in range(9, -1, -1):
        if int(k[on]) != table[0][on]:
            cnt += 1
            for dr, dc in (0, -1), (0, 1), (1, 0), (0, 0):
                nc = (9-on) + dc
                if 0 <= nc < 10:
                    table[dr][nc] ^= 1
    # 윗줄을 꺼주면서 내려감
    for i in range(1, 10):
        for j in range(10):
            if table[i - 1][j]:
                cnt += 1
                if cnt >= answer:
                    return
                for dr, dc in (0, -1), (0, 1), (1, 0), (-1, 0), (0, 0):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < 10 and 0 <= nc < 10:
                        table[nr][nc] ^= 1
    # 윗 줄은 다 꺼진 상태니까 마지막 줄만 확인해서 다 꺼졌다면 성공
    for check in range(10):
        if table[9][check]:
            return
    answer = cnt


switch = {'#': 0, 'O': 1}
arr = [list(map(lambda x: switch[x], input())) for _ in range(10)]

answer = 987654321
# 첫째줄을 누르는 모든 경우의 수
for t in range(1 << 10):
    solve(t)

print(answer if answer != 987654321 else -1)
