import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = ['.'] * (M+2)
mat = [arr] + [['.'] + list(input().rstrip()) + ['.'] for _ in range(N)] + [arr]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

sunk_list = []
for i in range(N+2):
    for j in range(M+2):
        if mat[i][j] == 'X':
            cnt = 0
            for k in range(4):
                r = i + dy[k]
                c = j + dx[k]
                if 0 <= r < N+2 and 0 <= c < M+2:
                    if mat[r][c] == '.':
                        cnt += 1
            if cnt >= 3:
                sunk_list.append((i, j))
for s in sunk_list:
    mat[s[0]][s[1]] = '.'

s = M+2
e = -1
rs = N+2
re = -1
for i in range(N+2):
    cnt = 0
    for j in range(M+2):
        if mat[i][j] == 'X':
            if j < s:
                s = j
            if j > e:
                e = j
            if i < rs:
                rs = i
            if i > re:
                re = i

new_mat = []
for i in range(N+2):
    if rs <= i < (re + 1):
        new_mat.append(mat[i])

new_mat2 = []
for i in range(len(new_mat)):
    new_mat2.append(new_mat[i][s:e+1])


for i in range(len(new_mat2)):
    ans = ''
    for j in range(len(new_mat2[i])):
        ans += new_mat2[i][j]
    print(ans)
