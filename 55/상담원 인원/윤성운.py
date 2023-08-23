import heapq

def solution(k, n, reqs):
    
    # 배치된대로 상담 진행
    def consult():
        nonlocal answer
        
        tmp = 0
        consult_dict = dict()
        for req in reqs:
            if req[2] not in consult_dict:
                consult_dict[req[2]] = [req[0] + req[1]]
                continue
            # 현재 상담 인원이 꽉 찼다면, 힙에서 가장 시간 적게 남은 인원 빼고 (남은 시간 + 내 상담 시간) 넣기
            if len(consult_dict[req[2]]) == selection[req[2] - 1]:
                if consult_dict[req[2]][0] > req[0]:
                    tmp += consult_dict[req[2]][0] - req[0]
                    before = heapq.heappop(consult_dict[req[2]])
                    heapq.heappush(consult_dict[req[2]], before + req[1])
                else:
                    heapq.heappop(consult_dict[req[2]])
                    heapq.heappush(consult_dict[req[2]], req[0] + req[1])
            else:
                heapq.heappush(consult_dict[req[2]], req[0] + req[1])
        if tmp < answer:
            answer = tmp        
    
    
    # n명의 상담원을 k개의 유형에 배치 (최소 한 명씩)
    def allocate(depth, acc):
        if depth == k - 1:
            selection[-1] = n - acc
            consult()
            return
    
        for i in range(1, n - k + 2):
            selection[depth] = i
            if acc + i >= n:
                return
            allocate(depth + 1, acc + i)
    
    
    # 각 상담 유형 별로 참가자 분류
    consult_dict = dict()
    for req in reqs:
        if req[2] in consult_dict:
            consult_dict[req[2]].append((req[0], req[1]))
        else:
            consult_dict[req[2]] = [(req[0], req[1])]
    
    selection = [0] * k
    answer = 987654321
    allocate(0, 0)
    
    return answer