def solution(a):

    # 최솟값과 인덱스 찾기
    min_num = 1000000001
    for i in range(len(a)):
        if a[i] < min_num:
            min_num = a[i]
            min_idx = i
    
    answer = 1

    # 왼쪽부터 보면서 현재까지의 최솟값 찾기
    left_min = 1000000001
    for i in range(min_idx):
        if a[i] < left_min:
            left_min = a[i]
            answer += 1 # 찾을 때마다 answer + 1
    
    # 오른쪽부터 보면서 현재까지의 최솟값 찾기
    right_min = 1000000001
    for i in range(len(a) - 1, min_idx, -1):
        if a[i] < right_min:
            right_min = a[i]
            answer += 1 # 찾을 때마다 answer + 1
    
    return answer