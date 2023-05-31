from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total = 0
    answer = 0
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    total = queue1_sum + queue2_sum
    stop = (len(queue1)+len(queue2)) * 2

    for i1 in range(len(queue1)):
        total += queue1[i1]
    for i2 in range(len(queue2)):
        total += queue2[i2]
    while True:
        if queue1_sum > queue2_sum:
            num = queue1.popleft()
            queue2.append(num)
            queue1_sum -= num
            queue2_sum += num
            answer += 1
        elif queue1_sum < queue2_sum:
            num = queue2.popleft()
            queue1.append(num)
            queue1_sum += num
            queue2_sum -= num
            answer += 1
        else:
            break
        # 한 아이템이 나갈때 1더하고
        if answer == stop:
            answer = -1
            break
    return answer
