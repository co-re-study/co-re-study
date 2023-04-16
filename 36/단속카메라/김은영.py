def solution(routes):
    answer = 0
    # 차량이 고속도로를 빠져나간 구간을 기준으로 정렬을 해준다.
    routes.sort(key = lambda x:x[1])
    # 현재 위치는 -30001로 지정
    current = -30001
    # 전체를 돌면서 카메라보다 앞에 앞에 있으면 카메라 위치를 시작점으로 옮기고 +1
    for route in routes:
        if route[0] > current:
            answer += 1
            current = route[1]
    
    return answer