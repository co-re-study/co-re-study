# 첫 번째 인덱스를 고르는 경우는 마지막 인덱스를 고르지 못함
# 마지막 인덱스를 고르는 경우는 첫 번째 인덱스를 고르지 못함
# 두 가지 모두 고려

def solution(sticker):
    
    # 예외처리
    if len(sticker) == 1:
        return sticker[0]
    
    # 첫 번째 인덱스를 골랐을 때
    # dp = [[현재 인덱스를 고른 경우, 현재 인덱스를 안 고른 경우], ...]
    dp = [[0, 0] for _ in range(len(sticker))]
    dp[0] = [sticker[0], 0]
    for i in range(1, len(sticker) - 1):
        dp[i][0] = dp[i - 1][1] + sticker[i] # 이전에 안 고른 경우에서 현재 스티커만큼 더하기
        dp[i][1] = max(dp[i - 1]) # 이전에 골랐든 안 골랐든 최댓값 가져오기
    answer = max(dp[-2])

    # 마지막 인덱스를 골랐을 때
    dp = [[0, 0] for _ in range(len(sticker))]
    dp[-1] = [sticker[-1], 0]
    for i in range(len(sticker) - 2, 0, -1):
        dp[i][0] = dp[i + 1][1] + sticker[i]
        dp[i][1] = max(dp[i + 1])

    # 마지막 인덱스를 고른 경우가 더 크면 답 변경    
    if max(dp[1]) > answer:
        answer = max(dp[1])

    return answer