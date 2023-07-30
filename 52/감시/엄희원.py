import sys
input = sys.stdin.readline
from copy import deepcopy
from itertools import permutations

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
mat2 = deepcopy(mat)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cam_list = []
wall = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] not in (0, 6, 7):
            cam_list.append((i, j))
        elif mat[i][j] == 6:
            wall += 1
ans = N*M - wall



def move(order, mat, cnt):
    global ans
    if order == len(cam_list):
        ans = min(ans, cnt)
        return
    i, j = cam_list[order]

    if mat[i][j] == 1:
        cnt -= 1
        for k in range(4):
            tmp = 0
            tmat = deepcopy(mat)
            r = i + dy[k]
            c = j + dx[k]
            while 0 <= r < N and 0 <= c < M:
                if tmat[r][c] == 6:
                    break
                elif tmat[r][c] == 0:
                    tmp += 1
                    tmat[r][c] = 7
                r += dy[k]
                c += dx[k]
            move(order+1, tmat, cnt - tmp)

    elif mat[i][j] == 2:
        cnt -= 1

        dir_list = [(0, 1), (2, 3)]
        for d in range(len(dir_list)):
            tmp = 0
            tmat = deepcopy(mat)
            for k in dir_list[d]:
                r = i + dy[k]
                c = j + dx[k]
                while 0 <= r < N and 0 <= c < M:
                    if tmat[r][c] == 6:
                        break
                    elif tmat[r][c] == 0:
                        tmp += 1
                        tmat[r][c] = 7
                    r += dy[k]
                    c += dx[k]
            move(order+1, tmat, cnt - tmp)

    elif mat[i][j] == 3:
        cnt -= 1

        dir_list = [(0, 3), (3, 1), (1, 2), (2, 0)]
        for d in range(len(dir_list)):
            tmp = 0
            tmat = deepcopy(mat)
            for k in dir_list[d]:
                r = i + dy[k]
                c = j + dx[k]
                while 0 <= r < N and 0 <= c < M:
                    if tmat[r][c] == 6:
                        break
                    elif tmat[r][c] == 0:
                        tmp += 1
                        tmat[r][c] = 7
                    r += dy[k]
                    c += dx[k]
            move(order + 1, tmat, cnt - tmp)

    elif mat[i][j] == 4:
        cnt -= 1

        dir_list = [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]
        for d in range(len(dir_list)):
            tmp = 0
            tmat = deepcopy(mat)
            for k in dir_list[d]:
                r = i + dy[k]
                c = j + dx[k]
                while 0 <= r < N and 0 <= c < M:
                    if tmat[r][c] == 6:
                        break
                    elif tmat[r][c] == 0:
                        tmp += 1
                        tmat[r][c] = 7
                    r += dy[k]
                    c += dx[k]
            move(order+1, tmat, cnt-tmp)
    elif mat[i][j] == 5:
        cnt -= 1

        tmp = 0
        for k in range(4):
            r = i + dy[k]
            c = j + dx[k]
            while 0 <= r < N and 0 <= c < M:
                if mat[r][c] == 6:
                    break
                elif mat[r][c] == 0:
                    tmp += 1
                    mat[r][c] = 7
                r += dy[k]
                c += dx[k]
        move(order+1, mat, cnt - tmp)

move(0, mat, ans)

print(ans)







# perm = list(permutations([1,2,3,4,5], 5))
#
# # ans = N*M
# ret = N*M
# # ans = N * M
# for pe in perm:
#     ans = N * M
#     mat = mat2
#     for p in pe:
#
#         for i, j in cam_list[p]:
#
#             if mat[i][j] == 6:
#                 ans -= 1
#
#             elif mat[i][j] == 1:
#                 ans -= 1
#                 temp = 0
#                 tmat_list = []
#                 max_tmp_idx = 0
#                 for k in range(4):
#                     tmp = 0
#                     tmat = deepcopy(mat)
#                     r = i + dy[k]
#                     c = j + dx[k]
#                     while 0 <= r < N and 0 <= c < M:
#                         if tmat[r][c] == 6:
#                             break
#                         elif tmat[r][c] == 0:
#                             tmp += 1
#                             tmat[r][c] = 7
#                         r += dy[k]
#                         c += dx[k]
#                     tmat_list.append(tmat)
#                     if tmp > temp:
#                         temp = tmp
#                         max_tmp_idx = k
#                 ans -= temp
#                 mat = tmat_list[max_tmp_idx]
#
#             elif mat[i][j] == 3:
#                 ans -= 1
#                 temp = 0
#                 tmat_list = []
#                 max_tmp_idx = 0
#                 dir_list = [(0, 3), (3, 1), (1, 2), (2, 0)]
#                 for d in range(len(dir_list)):
#                     tmp = 0
#                     tmat = deepcopy(mat)
#                     for k in dir_list[d]:
#                         r = i + dy[k]
#                         c = j + dx[k]
#                         while 0 <= r < N and 0 <= c < M:
#                             if tmat[r][c] == 6:
#                                 break
#                             elif tmat[r][c] == 0:
#                                 tmp += 1
#                                 tmat[r][c] = 7
#                             r += dy[k]
#                             c += dx[k]
#                     tmat_list.append(tmat)
#                     if tmp > temp:
#                         temp = tmp
#                         max_tmp_idx = d
#                 ans -= temp
#                 mat = tmat_list[max_tmp_idx]
#
#             elif mat[i][j] == 2:
#                 ans -= 1
#                 temp = 0
#                 tmat_list = []
#                 max_tmp_idx = 0
#                 dir_list = [(0, 1), (2, 3)]
#                 for d in range(len(dir_list)):
#                     tmp = 0
#                     tmat = deepcopy(mat)
#                     for k in dir_list[d]:
#                         r = i + dy[k]
#                         c = j + dx[k]
#                         while 0 <= r < N and 0 <= c < M:
#                             if tmat[r][c] == 6:
#                                 break
#                             elif tmat[r][c] == 0:
#                                 tmp += 1
#                                 tmat[r][c] = 7
#                             r += dy[k]
#                             c += dx[k]
#                     tmat_list.append(tmat)
#                     if tmp > temp:
#                         temp = tmp
#                         max_tmp_idx = d
#                 ans -= temp
#                 mat = tmat_list[max_tmp_idx]
#
#             elif mat[i][j] == 4:
#                 ans -= 1
#                 temp = 0
#                 tmat_list = []
#                 max_tmp_idx = 0
#                 dir_list = [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]
#                 for d in range(len(dir_list)):
#                     tmp = 0
#                     tmat = deepcopy(mat)
#                     for k in dir_list[d]:
#                         r = i + dy[k]
#                         c = j + dx[k]
#                         while 0 <= r < N and 0 <= c < M:
#                             if tmat[r][c] == 6:
#                                 break
#                             elif tmat[r][c] == 0:
#                                 tmp += 1
#                                 tmat[r][c] = 7
#                             r += dy[k]
#                             c += dx[k]
#                     tmat_list.append(tmat)
#                     if tmp > temp:
#                         temp = tmp
#                         max_tmp_idx = d
#                 ans -= temp
#                 mat = tmat_list[max_tmp_idx]
#
#
#             elif mat[i][j] == 5:
#                 ans -= 1
#                 for k in range(4):
#                     r = i + dy[k]
#                     c = j + dx[k]
#                     while 0 <= r < N and 0 <= c < M:
#                         if mat[r][c] == 6:
#                             break
#                         elif mat[r][c] == 0:
#                             ans -= 1
#                             mat[r][c] = 7
#                         r += dy[k]
#                         c += dx[k]
#     ret = min(ret, ans)
#
# # print(mat)
# # print(perm)
# print(ret - wall)


