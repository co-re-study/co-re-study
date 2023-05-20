from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    length = len(queue1)
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    total = sum_queue1 + sum_queue2
    # 총 합이 홀수면 볼 필요 x
    if total % 2:
        answer = -1

    # 그리디
    while answer != -1:
        # 합이 더 큰 큐에서 더 작은 큐로 이동
        if sum_queue1 > sum_queue2:
            pop_num = deque1.popleft()
            sum_queue1 -= pop_num
            deque2.append(pop_num)
            sum_queue2 += pop_num
            answer += 1
        elif sum_queue1 < sum_queue2:
            pop_num = deque2.popleft()
            sum_queue2 -= pop_num
            deque1.append(pop_num)
            sum_queue1 += pop_num
            answer += 1
        elif sum_queue1 == sum_queue2:
            break

        # ex)
        # [1, 1, 1, 1, 1], [1, 1, 1, 9, 1] (length = 5)
        # [1, 1, 1, 1, 1, 1, 1, 1], [9, 1]   -> length - 2
        # [], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1] -> length + length - 2
        # [9], [1, 1, 1, 1, 1, 1, 1, 1, 1]   -> 1
        # (length - 2) + (length + length - 2) + (1) = 3*length - 3
        if answer == length * 3 - 2:
            answer = -1

    return answer