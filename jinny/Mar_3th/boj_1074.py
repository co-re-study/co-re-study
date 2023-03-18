#  Z
import sys


def dc(n, x, y):
    global answer
    if x > r or r >= x+(2**n) or y > c or c >= y+(2**n):
        answer += (2 ** n) ** 2
        return
    if n == 1:
        for i in range(2):
            for j in range(2):
                if x+i == r and y+j == c:
                    print(answer)
                    sys.exit()
                else:
                    answer += 1
    else:
        for zr in range(2):
            for zc in range(2):
                dc(n-1, x+(2**n//2)*zr, y+(2**n//2)*zc)


n, r, c = map(int, input().split())
answer = 0
dc(n, 0, 0)
