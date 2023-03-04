import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def paperCheck(start_x, start_y, size):
    for r in range(start_x, start_x + size):
        for c in range(start_y, start_y + size):
            if paper[c][r] != paper[start_y][start_x]:
                for x in range(2):
                    for y in range(2):
                        paperCheck(start_x + x * (size // 2), start_y + y * (size // 2), size // 2)
                return
    paper_count[paper[c][r]] += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

paper_count = {0: 0, 1: 0}
paperCheck(0, 0, n)

for i in paper_count.values():
    print(i)