def solution(routes):
    answer = 0
    # 카메라 끝 지점 기준으로 정렬시킨 다음, 현재 시점이 해당 카메라 시작 지점보다
    # 왼쪽에 있으면 도착 지점으로 현재 시점을 변경시켜준다.  
    routes.sort(key=lambda x: x[1])
    current = -30001
    for route in routes:
        if current < route[0]:
            answer += 1
            current = route[1]
    return answer