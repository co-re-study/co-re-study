import sys

input = sys.stdin.readline
par_num, pardak_num = map(int, input().split())


par_list = []
sum_par = 0
left = 1
right = 0
for i in range(par_num):
    par = int(input())
    par_list.append(par)

    if par > right:
        right = par
    sum_par += par
answer = 0
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for par_length in par_list:
        cnt += par_length // mid

    if cnt >= pardak_num:
        left = mid+1
        answer = mid
    else:
        right = mid-1
rest_pieces = sum_par - answer*pardak_num
print(rest_pieces)


