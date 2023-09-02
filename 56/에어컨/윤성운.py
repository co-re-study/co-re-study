import heapq

def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    
    N = len(onboard)
    memo = [[[987654321] * 3 for _ in range(51)] for _ in range(N)]
    heap = [(0, 0, temperature, False, False), (0, 0, temperature, True, False)]
    heat_flow = 1 if temperature > t2 else -1
    
    while heap:
        acc, time, temp, is_on, is_same_temp = heapq.heappop(heap)
        
        # idx: 0(에어컨 off) / 1(에어컨 on, 희망온도 = 현재온도) / 2(에어컨 on, 희망온도 != 현재온도)
        idx = 2
        if is_on:
            if is_same_temp:
                acc += b
                idx = 0
            else:
                acc += a
                temp -= heat_flow
                idx = 1
        elif temp != temperature:
            temp += heat_flow
        time += 1
        
        if temp < 0 or temp >= 51:
            continue
        if onboard[time] and (temp < t1 or temp > t2):
            continue
        if memo[time][temp][idx] <= acc:
            continue
        memo[time][temp][idx] = acc
        
        if time == N - 1:
            continue
        
        heapq.heappush(heap, (acc, time, temp, False, False))
        heapq.heappush(heap, (acc, time, temp, True, True))
        heapq.heappush(heap, (acc, time, temp, True, False))
        
    answer = 987654321
    for i in range(51):
        answer = min(answer, min(memo[-1][i]))
            
    return answer