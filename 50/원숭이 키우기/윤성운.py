# c++ 풀이 복붙

import sys
input = sys.stdin.readline

N = int(input())
character_cnts = [0] + list(map(int, input().split()))
strs = [0] + list(map(int, input().split()))
D = int(input())

# 초기 사람 힘의 합 구하기
initial = 0
for i in range(1, N + 1):
    initial += character_cnts[i] * strs[i]
    # 사람 아무리 많아도 D일 밖에 이동하지 못하므로 값 조정
    character_cnts[i] = min(D, character_cnts[i])

# D일만큼의 dp 생성
dp = [0] * (D + 1)

# i: 현재 레벨
# j: 현재 지난 기간
# k: 다음 레벨
for i in range(1, N + 1):
    # 현재 레벨의 캐릭터 모두 훈련시키기
    while character_cnts[i]:
        for j in range(D, -1, -1):
            k = i + 1
            # 훈련시킬 수 있다면
            while k <= N and k + j - i <= D:
                # j일만큼 지났을 때 i레벨에서 k레벨로 가는게 이득인지 확인
                dp[k + j - i] = max(dp[k + j - i], dp[j] + strs[k] - strs[i])
                k += 1
        character_cnts[i] -= 1

print(initial + dp[-1])
