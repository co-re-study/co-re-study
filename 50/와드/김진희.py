import sys
# input = sys.stdin.readline           # 틀렸습니다
# input = sys.stdin.readline().rstrip  # 런타임 에러 (IndexError)
# input 시간 초과니까 -> 코드 자체에서 바꿔 .rstrip()까지! .strip()도 되는데 시간 쪼금 더 걸림


def dfs(x, y):
    stack = [(x, y)]
    # visited = {(x, y)}         # 시간초과
    while stack:
        cr, cc = stack.pop()
        # answer[cr][cc] = '.'   # 시간초과
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < r and 0 <= nc < c and answer[nr][nc] == "#" and arr[nr][nc] == arr[x][y]:
                answer[nr][nc] = '.'
                stack.append((nr, nc))


r, c = map(int, sys.stdin.readline().rstrip().split())    # 격자 크기
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
answer = [['#'] * c for _ in range(r)]
hr, hc = map(int, sys.stdin.readline().rstrip().split())  # 한별 위치
hr -= 1
hc -= 1
travel = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

for char in list(sys.stdin.readline().rstrip()):
    if char in travel:
        hr, hc = hr + travel[char][0], hc + travel[char][1]
    elif answer[hr][hc] == '#':
        answer[hr][hc] = '.'
        dfs(hr, hc)

# 현재 위치에서 보이는 곳 체크
answer[hr][hc] = '.'
for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    if 0 <= hr + dr < r and 0 <= hc + dc < c and answer[hr + dr][hc + dc] == '#':
        answer[hr + dr][hc + dc] = '.'

for i in answer:
    print(*i, sep='')
