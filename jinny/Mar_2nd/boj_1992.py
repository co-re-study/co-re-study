# 쿼드 트리
def quard(n, x, y): # 8
    square = "("
    for j in range(4):  # 0 1 2 3
        ans = 0
        for r in range(n//2):  # 0 1 2 3
            ans += sum(arr[(j // 2) * (n // 2) + r + x][j % 2 * (n // 2) + y: j % 2 * (n // 2) + n // 2 + y])
        if ans not in {(n//2)**2, 0}:
            square += (quard(n//2, (j // 2) * (n // 2) + x, j % 2 * (n // 2) + y))
        else:
            square += ("1" if ans else "0")
    return square+")"


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
answer = ""
count = 0
for i in range(n):
    count += sum(arr[i])
if count not in {n*n, 0}:
    answer += quard(n, 0, 0)
else:
    answer += "1" if count else "0"
print(answer)