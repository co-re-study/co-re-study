from collections import deque
def solution(food_times, k):
    answer = 0
    counts_dict = {}
    counts_list = []
    left_food = set()
    for i in range(len(food_times)):
        food_time = food_times[i]
        left_food.add(i+1)
        if food_time in counts_dict:
            counts_dict[food_time].append(i+1)
        else:
            counts_dict[food_time] = [i+1]
            counts_list.append(food_time)

    cycle = len(food_times)
    counts_list = deque(sorted(counts_list))
    rounds = 0
    while k and left_food:
        # k에 빨리 접근하기
        current_minimum = counts_list.popleft()
        print(k, current_minimum, left_food)
        if cycle * (current_minimum - rounds) <= k:
            k -= cycle * (current_minimum - rounds)
            rounds = current_minimum
            for idx in counts_dict[current_minimum]:
                left_food.discard(idx)
                cycle -= 1
        else:
            k %= cycle
            break

    if not left_food:
        return -1
    left_food = sorted(list(left_food))
    answer = left_food[k]

    return answer

print(solution([3, 1, 2], 5))