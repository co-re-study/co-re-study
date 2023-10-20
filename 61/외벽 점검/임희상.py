from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak.extend([w+n for w in weak])

    answer = len(dist) + 1
    
    for start in range(length):
        for friends in permutations(dist):
            count, position = 1, weak[start] + friends[0]
            
            for i in range(start, start + length):
                if position < weak[i]:
                    if count == len(friends):
                        break
                    count += 1
                    position = weak[i] + friends[count - 1]
            else:
                answer = min(answer, count)

    return -1 if answer > len(dist) else answer