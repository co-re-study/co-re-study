def solution(stones, k):
    lens = len(stones)
    return min(max(stones[x:x+k]) for x in range(lens-k+1))
