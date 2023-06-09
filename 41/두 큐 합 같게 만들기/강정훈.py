from collections import deque
def rolling_queue(queue1, queue2):
    cnt = 0
    flag = False
    queue1_hap = sum(queue1)
    queue2_hap = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while True:
        if queue1_hap > queue2_hap:
            queue1_pop = queue1.popleft()
            queue2.append(queue1_pop)
            queue1_hap -= queue1_pop
            queue2_hap += queue1_pop
            cnt +=1
        elif queue1_hap < queue2_hap:
            queue2_pop = queue2.popleft()
            queue1.append(queue2_pop)
            queue1_hap += queue2_pop
            queue2_hap -= queue2_pop
            cnt += 1
        else:
            flag = True
            return flag, cnt
        if cnt == len(queue1)*4:
            return flag, cnt





def solution(queue1, queue2):
    flag, cnt = rolling_queue(queue1,queue2)
    if flag:
        answer = cnt
    else:
        answer = -1

    return answer

queue1= [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1,queue2))
