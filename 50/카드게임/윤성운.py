import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(left_idx, right_idx):
    if left_idx == N or right_idx == N:
        return 0
    
    # 이미 체크한 값이면 바로 반환
    if dp[left_idx][right_idx] > -1:
        return dp[left_idx][right_idx]
    
    # 왼쪽 카드가 오른쪽 카드보다 크거나 같으면, 왼쪽 카드만 넘기거나 둘 다 넘기기
    if left_cards[left_idx] <= right_cards[right_idx]:
        dp[left_idx][right_idx] = max(dfs(left_idx + 1, right_idx), dfs(left_idx + 1, right_idx + 1))
    # 왼쪽 카드가 오른쪽 카드보다 작으면, 오른쪽 카드만 넘기고 점수 누적
    else:
        dp[left_idx][right_idx] = dfs(left_idx, right_idx + 1) + right_cards[right_idx]

    return dp[left_idx][right_idx]
    


N = int(input())
left_cards = list(map(int, input().split()))
right_cards = list(map(int, input().split()))

dp = [[-1] * N for _ in range(N)]
dfs(0, 0)

print(dp[0][0])