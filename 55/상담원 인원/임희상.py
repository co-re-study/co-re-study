import heapq
from collections import deque
        
def solution(k, n, reqs):
    answer = float('inf')
    mentors = [1] * k
    
    def mentor_combination(idx, left):
        nonlocal mentors
    
        if idx == k-1:
            mentors[idx] += left
            
            simulate()
            mentors[idx] -= left
            return
        
        for i in range(left+1):
            mentors[idx] += i
            mentor_combination(idx+1, left-i)
            mentors[idx] -= i
    
    def simulate():
        nonlocal answer
        
        waiting = [deque() for _ in range(k)]
        available = mentors[:]
        for req in reqs:
            mentor = req[2] - 1
            waiting[mentor].append(req)
        
        total_waiting = 0
        
        for mentor in range(k):
            
            heap = []
            while available[mentor]:
                
                if not waiting[mentor]:
                    break
                    
                start, duration, tmp = waiting[mentor].popleft()
                heapq.heappush(heap, start+duration)
                available[mentor] -= 1
                
            while heap and waiting[mentor]:
                
                end = heapq.heappop(heap)
                next_start, duration, tmp = waiting[mentor].popleft()
                total_waiting += max(0, end - next_start)
                heapq.heappush(heap, max(end, next_start) + duration)
        answer = min(answer, total_waiting)
    
    mentor_combination(0, n-k)
    
    return answer