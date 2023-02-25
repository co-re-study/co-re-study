# 비밀번호 찾기
from collections import defaultdict
N, M = map(int, input().split())
memo = defaultdict()
for _ in range(N):
    address, password = input().split()
    memo[address] = password
for _ in range(M):
    print(memo[input()])