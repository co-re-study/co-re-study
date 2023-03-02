import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def paperCheck(start_x, start_y, size):
    for r in range(start_x, start_x + size):                # size 크기의 종이를 순회
        for c in range(start_y, start_y + size):
            if paper[r][c] != paper[start_x][start_y]:      # 종이가 같은 숫자로만 이루어 져있지 않으면
                for x in range(3):                          # 종이를 잘라서
                    for y in range(3):
                        paperCheck(start_x + x * (size // 3), start_y + y * (size // 3), size // 3)     # 종이 순회
                return

    number_count[paper[r][c]] += 1                          # 같은 숫자로만 이루어져있으면 해당 숫자의 개수 +1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
number_count = {-1: 0, 0: 0, 1: 0}

paperCheck(0, 0, n)

for i in range(-1, 2, 1):
    print(number_count[i])