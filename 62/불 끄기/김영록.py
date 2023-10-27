def switch(x, y):
    global temp
    for i in range(5):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < 10 and 0 <= y1 < 10:
            temp_arr[x1][y1] = 'O' if temp_arr[x1][y1] == '#' else '#'
    temp += 1


dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
arr = [list(input()) for _ in range(10)]
ans = 1000
for i in range(1 << 10):
    temp_arr = [arr[i][:] for i in range(10)]
    temp = 0
    for j in range(10):
        if i & (1 << j):
            switch(0, j)
    for k in range(1, 10):
        for l in range(10):
            if temp_arr[k-1][l] == 'O':
                switch(k, l)
    for p in range(10):
        if temp_arr[9][p] == "O":
            break
    else:
        ans = min(ans, temp)
print(ans if ans != 1000 else -1)
