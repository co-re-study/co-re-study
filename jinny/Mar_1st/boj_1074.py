# Z
def dc(n, x, y):
    global answer
    global flag
    if n == 1:
        for i in range(2):
            if flag:
                return
            for j in range(2):
                arr[x+i][y+j] = answer
                if x+i == r and y+j == c:
                    print(answer)
                    flag = 1
                answer += 1
    else:
        for zr in range(2):
            if flag:
                return
            for zc in range(2):
                dc(n-1, x+(2**n//2)*zr, y+(2**n//2)*zc)


n, r, c = map(int, input().split())
arr = [[0] * (2**n) for _ in range(2 ** n)]
answer = 0
flag = 0
dc(n, 0, 0)
