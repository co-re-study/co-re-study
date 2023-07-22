import sys
sys.setrecursionlimit(10**4)

def play(score=0, l=0, r=0):
    global ans, count
    count += 1

    if l == N or r == N:
        ans = max(ans, score)
        return
    
    if dp[l][r] >= score:
        return
    
    dp[l][r] = score

    if left[l] > right[r]:
        play(score + right[r], l, r + 1)
    play(score, l + 1, r)
    play(score, l + 1, r + 1)

N, left, right = int(input()), list(map(int, input().split())), list(map(int, input().split()))
dp = [[-1 for i in range(N)] for j in range(N)]
count = 0
ans = 0
play()
print(ans)