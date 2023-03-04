# 색종이 만들기
def mollu(length, x, y):
    for r in range(x, x + length, length//2):
        for c in range(y, y + length, length//2):
            check_num = arr[r][c]
            def_flag = 0
            for inner_i in range(length//2):
                for inner_j in range(length//2):
                    if arr[r + inner_i][c + inner_j] != check_num:
                        mollu(length//2, r, c)
                        def_flag = 1
                        break
                if def_flag:
                    break
            else:
                count_dict[check_num] += 1
               

count_dict = {0: 0, 1: 0}
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
first_num = arr[0][0]

flag = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != first_num:
            mollu(n, 0, 0)
            flag = 1
            break
    if flag:
        break
else:
    count_dict[first_num] += 1
print(count_dict[0])
print(count_dict[1])
