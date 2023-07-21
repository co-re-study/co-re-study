
# 45%에서 틀렸는데 왜 안 되나..
# Top down으로는 안됨?
import sys
input=sys.stdin.readline

N = int(input())
left_cards = [0] + list(map(int, input().split()))
right_cards = [0] + list(map(int, input().split()))
points = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 1차원은 왼쪽카드, 2차원은 오른쪽카드 순서
for row in range(1,N+1):
    for col in range(1,N+1):
        if right_cards[col] < left_cards[row]:
            points[row][col] = max(points[row][col-1] + right_cards[col], points[row-1][col], points[row-1][col-1])
        else:
            points[row][col] = max(points[row-1][col], points[row-1][col-1])

print(points[N][N])