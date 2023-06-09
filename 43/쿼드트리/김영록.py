import sys
input = sys.stdin.readline
N = int(input())
img = [list(map(int, input().strip())) for _ in range(N)]


def Quad(x, y, n):
    first = img[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != img[i][j]:
                print('(', end='')
                n = n//2
                Quad(x, y, n)
                Quad(x, y+n, n)
                Quad(x+n, y, n)
                Quad(x+n, y+n, n)
                print(')', end='')
                return
    if first == 1:
        print(1, end='')
        return
    else:
        print(0, end='')
        return


Quad(0, 0, N)
