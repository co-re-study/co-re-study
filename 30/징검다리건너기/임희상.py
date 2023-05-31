from collections import deque
import heapq
def solution(stones, k):
    # 기본 로직은 슬라이딩 윈도우를 사용해 그 안의 최댓값을 찾아주는 것
    # 윈도우 내의 최댓값을 추적하며 최댓값이 윈도우를 빠져나갈 때 최댓값을 찾아줌
    # 단순히 max(윈도루)로 찾으면 케이스 한개 시간초과
    # 따라서 자료구조를 여러개 사용해서 윈도우 내에 최댓값을 잘 찾을 수 있게 함
    answer = 0
    heap = [-i for i in stones[:k]]  # 최댓값을 찾기 위한 힙
    heapq.heapify(heap)
    print(heap)
    queue = deque(stones[:k])
    current_max = max(queue)
    current_dict = {}  # 윈도우에 들어있는 값들을 기록
    for number in queue:
        if number in current_dict.keys():
            current_dict[number] += 1
        else:
            current_dict[number] = 1

    answer = current_max
    for stone in stones[k:]:
        out = queue.popleft()
        current_dict[out] -= 1
        queue.append(stone)
        if stone in current_dict.keys():
            current_dict[stone] += 1
        else:
            current_dict[stone] = 1
        if out == current_max:
            # 최댓값이 나갔을 때 새로운 최댓값을 찾는 법
            # 힙에서 최댓값을 꺼내면 새로운 최댓값이 다시 힙의 꼭대기로 올라옴
            # 힙의 꼭대기에 올라온 값이 윈도우 딕셔너리에 없다면
            # 윈도우에 있는 값이 보일때 까지 힙에서 최댓값을 꺼낸다.
            while True:
                heapq.heappop(heap)
                heap_max = -heap[0]
                if current_dict[heap_max]:
                    break
        heapq.heappush(heap, -stone)
        current_max = -heap[0]
        if answer > current_max:
            answer = current_max
        if stone > current_max:
            current_max = stone

    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	, 3)