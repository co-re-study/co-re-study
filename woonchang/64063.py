def solution(k, room_number):
    answer = []
    rooms = set()
    speedict = dict()
    target = 0
    for idx in range(len(room_number)):
        target = room_number[idx]
        if room_number[idx] in rooms:
            while target in rooms:
                target += 1
        rooms.add(target)
        answer.append(target)
    return answer
