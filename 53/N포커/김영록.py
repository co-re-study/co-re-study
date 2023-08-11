'''
포함배제
포카드 홀수일때는 더하고 짝수일때는 빼고
벤다이어그램 겹치는거 빼는 느낌으로 생각하기
'''
from math import comb
N = int(input())
mod = 10007
ans = 0
for i in range(1, 14):
    if N >= 4*i:
        if i % 2:
            ans = (ans + comb(52-4*i, N-4*i)*comb(13, i)) % mod
        else:
            ans = (ans - comb(52-4*i, N-4*i)*comb(13, i)) % mod
print(ans)
