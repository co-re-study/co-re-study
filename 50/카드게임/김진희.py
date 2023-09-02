import sys
sys.setrecursionlimit(10**6)


def card_game(r, c):
    # 카드덱 다 쓰면 return
    if r > n-1 or c > n-1:
        return 0
    # 배열로 쳤을 때, 점수 딴다면 c+1에서 카드만큼 더해오는 값
    # 점수를 안 딴다면 r+1 or r+1, c+1에서 점수 없이 오는 것이므로 그냥 더 큰값 가져오기
    if dp[r][c] == -1:
        dp[r][c] = card_game(r, c+1) + right[c] if left[r] > right[c] else max(card_game(r+1, c+1), card_game(r+1, c))
    return dp[r][c]  # 값이 없었을 때, 계산해서 생겼다면 이것도 return해줘야지


n = int(input())  # 카드 수
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[-1]*n for _ in range(n)]  # 0으로 하면 탐색했는지 안 했는지 몰라서 또 할 수 있음

print(card_game(0, 0))