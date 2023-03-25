# 최소 값을 찾은 다음
# 그 전 후로 k 만큼 움직이면서 최소값보다 크면서 제일 작은 값을 찾는다.

def solution(stones, k):
    # 효율성 배제 풀이
    mid = len(stones) // 2
    answer = max(stones)
    for i in range(mid):
        if i > (mid - k):
            answer = min(max(stones[i:i+k]), answer)
        else:
            answer = min(max(stones[i:i+k]), answer, max(stones[mid+i:mid+i+k]))
    
    # 이진탐색 말고는 답이 없는 듯
    
    return answer