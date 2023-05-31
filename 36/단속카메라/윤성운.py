# 현재 가장 마지막에 설치할 수 있는 CCTV보다 더 늦게 진입하면 정답 + 1 & CCTV 위치 갱신
# 현재 가장 마지막에 설치할 수 있는 CCTV보다 더 빨리 진입하지만 더 늦게 나가면 CCTV 위치만 갱신

def solution(routes):
    routes.sort(key=lambda x: x[0])
    current_finish = -30001
    answer = 0
    for route in routes:
        if route[0] > current_finish:
            answer += 1
            current_finish = route[1]
        elif route[1] < current_finish:
            current_finish = route[1]
        
    return answer