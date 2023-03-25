n = int(input())
m = int(input())
text = input()

ioi = 0
cnt = 0
idx = 0
while idx < m - 1:
    if text[idx:idx + 3] == 'IOI':
        idx += 2
        ioi += 1
        if ioi == n:
            cnt += 1
            ioi -= 1
    else:
        idx += 1
        ioi = 0

print(cnt)