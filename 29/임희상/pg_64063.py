def solution(k, room_number):
    answer = []
    portal = {}
    for request in room_number:
        path = [request]
        if request not in portal.keys():
            answer.append(request)
            portal[request] = request+1
        else:
            current = portal[request]
            while True:
                path.append(current)
                if current not in portal.keys():
                    answer.append(current)
                    destination = current + 1
                    for start in path:
                        portal[start] = destination
                    break
                current = portal[current]
    print(answer)
    return answer

solution(10, [1,3,4,1,3,1]	)